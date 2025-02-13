import read, copy
from util import *
from logical_classes import *

verbose = 0

class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        self.ie = InferenceEngine()

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB
        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be added
        Returns:
            None
        """
        printv("Adding {!r}", 1, verbose, [fact_rule])
        if isinstance(fact_rule, Fact):
            if fact_rule not in self.facts:
                self.facts.append(fact_rule)
                for rule in self.rules:
                    self.ie.fc_infer(fact_rule, rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.facts.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.facts[ind].supported_by.append(f)
                else:
                    ind = self.facts.index(fact_rule)
                    self.facts[ind].asserted = True
        elif isinstance(fact_rule, Rule):
            if fact_rule not in self.rules:
                self.rules.append(fact_rule)
                for fact in self.facts:
                    self.ie.fc_infer(fact, fact_rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.rules.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.rules[ind].supported_by.append(f)
                else:
                    ind = self.rules.index(fact_rule)
                    self.rules[ind].asserted = True

    def kb_assert(self, fact_rule):
        """Assert a fact or rule into the KB

        Args:
            fact_rule (Fact or Rule): Fact or Rule we're asserting
        """
        printv("Asserting {!r}", 0, verbose, [fact_rule])
        self.kb_add(fact_rule)

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        if factq(fact):
            f = Fact(fact.statement)
            bindings_lst = ListOfBindings()
            # ask matched facts
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else []

        else:
            print("Invalid ask:", fact.statement)
            return []

    def kb_retract(self, fact_rule):
        """Retract a fact or a rule from the KB

        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be retracted

        Returns:
            None
        """
        printv("Retracting {!r}", 0, verbose, [fact_rule])
        ####################################################
        # Student code goes here

        # Call retract helpers - two cases: fact and rule
        if isinstance(fact_rule, Fact):
            self.retract_fact(fact_rule)
        elif isinstance(fact_rule, Rule):
            self.retract_rule(fact_rule)


    def retract_fact(self, fact):
        """
        Helper to retract a fact
        """
        #There are three things to consider: the fact is not in the KB, 
        #the fact is asserted -> have to mark it unasserted, and removing it 
        #from the KB if it has no supports

        extracted_fact = self._get_fact(fact)

        # 1. fact not in KB
        if not extracted_fact:
            return  

        # 2. fact is asserted -> mark it unasserted 
        if extracted_fact.asserted:
            extracted_fact.asserted = False

        # 3. remove from KB in the case where the fact has no supports
        if len(extracted_fact.supported_by) == 0:
            self.facts.remove(extracted_fact)
            self.remove_supports(extracted_fact) 


    def retract_rule(self, rule):
        """
        Helper to retract a rule - identical logic to retract_fact
        """
        #IDENTICAL TO retract_fact

        extracted_rule = self._get_rule(rule)

        if not extracted_rule:
            return  

        if extracted_rule.asserted:
            extracted_rule.asserted = False

        if len(extracted_rule.supported_by) == 0:
            self.rules.remove(extracted_rule)
            self.remove_supports(extracted_rule)


    def remove_supports(self, target_remove_supports):
        """
        Helper to scan and remove facts/roles supported by the parent argument,
        recursive-based
        """

        # Call remove supports helpers - two cases: fact and rule 
        self.remove_supported_facts(target_remove_supports)
        self.remove_supported_rules(target_remove_supports)


    def remove_supported_facts(self, parent):
        """
        Helper to remove supported facts
        """
        #Loop through facts supported by the parent, first remove the parent
        #from the fact's supports. Then, if the fact has no other supports and 
        #isn't asserted, we can remove it. Continue the search by recursively 
        #removing stuff that the fact was supporting 

        for child_fact in parent.supports_facts:
            self._remove_parent_from_supported_by(child_fact, parent)

            if (len(child_fact.supported_by) == 0) and not child_fact.asserted:
                self.facts.remove(child_fact)
                self.remove_supports(child_fact)


    def remove_supported_rules(self, parent):
        """
        Helper to remove supported rules - identical logic to remove_supported_facts
        """
        #IDENTICAL TO remove_supported_facts

        for child_rule in parent.supports_rules:
            self._remove_parent_from_supported_by(child_rule, parent)

            if (len(child_rule.supported_by) == 0) and not child_rule.asserted:
                self.rules.remove(child_rule)
                self.remove_supports(child_rule)


    def _remove_parent_from_supported_by(self, child, parent):
        """
        Helper to remove parent from child's support list 
        """
        #Simply remove parent from the child.supported_by list 

        new = []
        for pair in child.supported_by:
            if parent not in pair:
                new.append(pair)
        child.supported_by = new


class InferenceEngine(object):
    def fc_infer(self, fact, rule, kb):
        """Forward-chaining to infer new facts and rules

        Args:
            fact (Fact) - A fact from the KnowledgeBase
            rule (Rule) - A rule from the KnowledgeBase
            kb (KnowledgeBase) - A KnowledgeBase

        Returns:
            Nothing
        """
        printv('Attempting to infer from {!r} and {!r} => {!r}', 1, verbose,
            [fact.statement, rule.lhs, rule.rhs])
        ####################################################
        # Student code goes here

        binds = match(rule.lhs[0], fact.statement)
        if binds:
            if len(rule.lhs) == 1:
                # Infer a new fact using the rule's RHS
                self.infer_new_fact(fact, rule, kb, binds)
            else:
                # Infer a "curried" new rule
                self.infer_new_rule(fact, rule, kb, binds)

    def infer_new_fact(self, source_fact, source_rule, kb, bindings):
        """
        Helper method to create a new Fact 
        """

        #First, instantiate the rule's RHS statement with the matched bindings
        #Create the new fact with the RHS statement and its supports (it's INFERRED, NOT asserted)
        #Lastly, add fact and mark that the source fact and rule support this new fact

        rhs_statement = instantiate(source_rule.rhs, bindings)
        
        new_fact = Fact(rhs_statement, supported_by=[[source_fact, source_rule]])
        
        new_fact.asserted = False  

        kb.kb_add(new_fact)

        source_fact.supports_facts.append(new_fact)
        source_rule.supports_facts.append(new_fact)

    def infer_new_rule(self, source_fact, source_rule, kb, bindings):
        """
        Helper method to create a new rule
        """
        
        #Similar logic to infer_new_fact...
        #First, remove the matched statement from the rule's LHS and instantiate 
        # the remaining LHS statements plus the RHS with the given bindings
        #Next, create the new rule with this updated LHS and RHS and mark it as INFERRED, NOT asserted
        #Lastly, add rule and mark that the source fact and rule support this new fact
        new_lhs = [instantiate(stmt, bindings) for stmt in source_rule.lhs[1:]]
        new_rhs = instantiate(source_rule.rhs, bindings)

        new_rule = Rule([new_lhs, new_rhs], supported_by=[[source_fact, source_rule]])
        
        new_rule.asserted = False  

        kb.kb_add(new_rule)

        source_fact.supports_rules.append(new_rule)
        source_rule.supports_rules.append(new_rule)