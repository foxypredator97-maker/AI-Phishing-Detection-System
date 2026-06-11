def calculate_trust_score(features):

    score = 100

    if features["url_length"] > 50:
        score -= 15

    if features["isHttps"] == 0:
        score -= 20

    if features["at_symbol"] > 0:
        score -= 15

    if features["nb_dots"] > 3:
        score -= 10

    if features["sensitive_words_count"] > 0:
        score -= 20

    if features["nb_hyphens"] > 0:
        score -= 10

    return max(score, 0)