moves_dict = {
    0: "Establishing the research territory",
    1: " Establishing the niche",
    2: "Occupying the niche",
}
sub_moves_dict = {
    0: {
        0: "Show that the research area is important, problematic, or relevant in some way",
        1: "Introduce and review previous research in the field",
    },
    1: {
        0: "Claim something is wrong with the previous research",
        1: "Highlight a gap in the field",
        2: "Raise a question where research in field is unclear",
        3: "Extend prior research to add more information on the topic",
    },
    2: {
        0: "Outline your purpose (s) and state the nature of your research",
        1: "State your hypothesis or research question you seek to answer",
        2: "Share your findings",
        3: "Elaborate on the value of your research",
        4: "Outline the structure that the research paper will follow",
    },
}


def map_move(move: int):
    return moves_dict[move]


def map_sub_move(move: int, sub_move: int):
    return sub_moves_dict[move][sub_move]
