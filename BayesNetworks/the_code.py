def probability_recursive(variables, known_values, bn): 
    if not variables: 
        return 1
    next_var= variables[0].name
    remaining_vars = variables[1:]
    node = bn.get_var(next_var)
    if next_var in known_values: 
        prob = node.probability(known_values[next_var], known_values)
        return prob * probability_recursive(remaining_vars, known_values, bn)
    else: 
        known_values[next_var] = True 
        prob_true = node.probability(True, known_values)
        prob_true_case_total = prob_true * probability_recursive(remaining_vars, known_values, bn)
            
        prob_false = node.probability(False, known_values)
        known_values[next_var] = False
        prob_false_case_total = prob_false * probability_recursive(remaining_vars, known_values, bn)
            
            
        del known_values[next_var]
        return prob_true_case_total + prob_false_case_total

def ask(var, value, evidence, bn):
    list_variables = bn.variables

    evidence[var] = value  
    prob_hypothesis_given_evidence = probability_recursive(list_variables, evidence, bn)
    
    evidence[var] = not value
    prob_neg_hypothesis_given_evidence = probability_recursive(list_variables, evidence, bn)
    
    alpha = prob_hypothesis_given_evidence + prob_neg_hypothesis_given_evidence
    
    return prob_hypothesis_given_evidence / alpha 

