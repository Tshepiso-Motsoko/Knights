from logic import *

# Symbols representing each character's nature.
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave.
    Not(And(AKnight, AKnave)),  # A cannot be both a knight and a knave.
    Biconditional(AKnight, And(AKnight, AKnave))  # If A is a knight, then A's statement is true; otherwise, it's false.
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),  # A cannot be both a knight and a knave.
    Not(And(BKnight, BKnave)),  # B cannot be both a knight and a knave.
    Biconditional(AKnight, And(AKnave, BKnave))  # A's statement is true if A is a knight, false otherwise.
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),  # A cannot be both a knight and a knave.
    Not(And(BKnight, BKnave)),  # B cannot be both a knight and a knave.
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),  # A's statement is true if both are the same kind.
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))  # B's statement is true if both are different kinds.
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don’t know which.
# B says "A said 'I am a knave.'"
# B then says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Implication(BKnight, And(Implication(AKnight, AKnave), CKnave)),  # If B is a knight, then A's claim (if A is a knight) is A is a knave, and C is a knave.
    Implication(BKnave, Or(Not(Implication(AKnight, AKnave)), CKnight)),  # If B is a knave, then either A didn't claim to be a knave, or C is a knight.
    Implication(CKnight, AKnight),  # If C is a knight, then A is a knight.
    Implication(CKnave, Not(AKnight))  # If C is a knave, then A is not a knight.
)


def main():
    # List all symbols for easy iteration.
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]

    # List all knowledge bases for easy iteration.
    knowledge_bases = [knowledge0, knowledge1, knowledge2, knowledge3]

    # Iterate over all puzzles.
    for i, knowledge in enumerate(knowledge_bases):
        print(f"Puzzle {i}:")

        # Check for each character if it is a Knight or Knave.
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"{symbol}: True")
            else:
                print(f"{symbol}: False")
        print()

if __name__ == "__main__":
    main()
