from sklearn.ensemble import RandomForestClassifier


def build_classifier() -> RandomForestClassifier:
    return RandomForestClassifier(n_estimators=120, random_state=42, class_weight='balanced')
