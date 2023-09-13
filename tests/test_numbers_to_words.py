from readability_improver.readability_improver import UnreadableFile

def test_ints():
    test_vecs = [
        (0, "ZERO"),
        (1, "ONE"),
        (2, "TWO"),
        (3, "THREE"),
        (4, "FOUR"),
        (5, "FIVE"),
        (6, "SIX"),
        (7, "SEVEN"),
        (8, "EIGHT"),
        (9, "NINE"),
        (10, "TEN"),
        (11, "ELEVEN"),
        (20, "TWENTY"),
        (21, "TWENTY_ONE"),
        (30, "THIRTY"),
        (31, "THIRTY_ONE"),
        (100, "ONE_HUNDRED"),
        (101, "ONE_HUNDRED_AND_ONE"),
    ]
    for stim, exp in test_vecs:
        assert UnreadableFile.number_to_word(stim) == exp

def test_floats():
    test_vecs = [
        (0.0, "ZERO_POINT_ZERO"),
        (1.0, "ONE_POINT_ZERO"),
        (0.00, "ZERO_POINT_ZERO"),
        (1.00, "ONE_POINT_ZERO"),
        (1.01, "ONE_POINT_ZERO_ONE"),
        (1.10, "ONE_POINT_ONE"),
        (1.11, "ONE_POINT_ONE_ONE"),
    ]

    for stim, exp in test_vecs:
        assert UnreadableFile.number_to_word(stim) == exp
