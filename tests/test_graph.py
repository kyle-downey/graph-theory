from graph import Graph


def graph01():
    """
    :return: Graph.
    """
    d = {1: {2: 10, 3: 5},
         2: {4: 1, 3: 2},
         3: {2: 3, 4: 9, 5: 2},
         4: {5: 4},
         5: {1: 7, 4: 6}}
    return Graph(from_dict=d)


def graph02():
    """
    1 -> 2 -> 3
    |    |    |
    v    v    v
    4 -> 5 -> 6
    |    |    |
    v    v    v
    7 -> 8 -> 9

    :return: :return:
    """
    d = {1: {2: 1, 4: 1},
         2: {3: 1, 5: 1},
         3: {6: 1},
         4: {5: 1, 7: 1},
         5: {6: 1, 8: 1},
         6: {9: 1},
         7: {8: 1},
         8: {9: 1}
         }
    return Graph(from_dict=d)


def graph03():
    d = {1: {2: 1, 3: 9, 4: 4, 5: 13, 6: 20},
         2: {1: 7, 3: 7, 4: 2, 5: 11, 6: 18},
         3: {8: 20, 4: 4, 5: 4, 6: 16, 7: 16},
         4: {8: 15, 3: 4, 5: 9, 6: 11, 7: 21},
         5: {8: 11, 6: 2, 7: 17},
         6: {8: 9, 7: 5},
         7: {8: 3},
         8: {7: 5}}
    return Graph(from_dict=d)


def graph04():
    d = {1: {2: 1, 3: 9, 4: 4, 5: 11, 6: 17},
         2: {1: 7, 3: 7, 4: 2, 5: 9, 6: 15},
         3: {8: 17, 4: 4, 5: 4, 6: 14, 7: 13},
         4: {8: 12, 3: 4, 5: 9, 6: 9, 7: 18},
         5: {8: 9, 6: 2, 7: 15},
         6: {8: 9, 7: 5},
         7: {8: 3},
         8: {7: 5}}
    return Graph(from_dict=d)


def graph05():
    """
    0 ---- 1 ---- 5
     +      +---- 6 ---- 7
      +            +     |
       +            +---- 8
        +
         +- 2 ---- 3 ---- 9
             +      +     |
              4      +---10
    """
    links = [
        (0, 1, 1),
        (0, 2, 1),
        (1, 5, 1),
        (1, 6, 1),
        (2, 3, 1),
        (2, 4, 1),
        (3, 9, 1),
        (3, 10, 1),
        (9, 10, 1),
        (6, 7, 1),
        (6, 8, 1),
        (7, 8, 1),
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1),
    ]
    return Graph(from_list=links)


def graph_cycle_5():
    """ cycle of 5 nodes """
    links = [
        (1, 2, 1),
        (2, 3, 1),
        (3, 4, 1),
        (4, 5, 1),
        (5, 1, 1),
    ]
    links.extend([(n2, n1, d) for n1, n2, d in links])
    return Graph(from_list=links)


def graph_cycle_6():
    """
    cycle of 6 nodes
    """
    links = [
        (1, 2, 1),
        (2, 3, 1),
        (3, 4, 1),
        (4, 5, 1),
        (5, 6, 1),
        (6, 1, 1),
    ]
    links.extend([(n2, n1, d) for n1, n2, d in links])
    return Graph(from_list=links)


def fully_connected_4():
    """
    fully connected graph with 4 nodes.
    """
    L = [
        (0, 3, 1), (0, 2, 1), (0, 1, 1), (3, 2, 1), (3, 1, 1), (3, 0, 1),
        (2, 3, 1), (2, 1, 1), (2, 0, 1), (1, 0, 1), (1, 2, 1), (1, 3, 1),
        (0,), (1,), (2,), (3,)
    ]
    g = Graph(from_list=L)
    return g


def mountain_river_map():
    """ Detailed mountain river map. Contributed by Harry Darby & Hartmut Mause """
    L = [(0,), (0, 164, 1), (1,), (1, 235, 1), (2,), (2, 1, 1), (3,), (3, 196, 1), (4,), (4, 3, 1), (5,), (5, 225, 1),
         (6,), (6, 5, 1), (7,), (7, 5, 1), (8,), (8, 211, 1), (9,), (9, 8, 1), (10,), (10, 144, 1), (11,), (11, 10, 1),
         (12,), (12, 234, 1), (13,), (13, 12, 1), (14,), (14, 172, 1), (15,), (15, 14, 1), (16,), (16, 14, 1), (17,),
         (17, 184, 1), (18,), (18, 17, 1), (19,), (19, 226, 1), (20,), (20, 19, 1), (21,), (21, 14, 1), (22,),
         (22, 222, 1), (23,), (23, 22, 1), (24,), (24, 240, 1), (25,), (25, 24, 1), (26,), (26, 241, 1), (27,),
         (27, 26, 1), (28,), (28, 71, 1), (29,), (29, 28, 1), (30,), (30, 28, 1), (31,), (31, 198, 1), (32,),
         (32, 31, 1), (33,), (33, 67, 1), (34,), (34, 33, 1), (35,), (35, 247, 1), (36,), (36, 35, 1), (37,),
         (37, 194, 1), (38,), (38, 37, 1), (39,), (39, 193, 1), (40,), (40, 39, 1), (41,), (41, 39, 1), (42,),
         (42, 39, 1), (43,), (43, 230, 1), (44,), (44, 43, 1), (45,), (45, 233, 1), (46,), (46, 45, 1), (47,),
         (47, 238, 1), (48,), (48, 47, 1), (49,), (49, 47, 1), (50,), (50, 215, 1), (51,), (51, 50, 1), (52,),
         (52, 166, 1), (53,), (53, 52, 1), (54,), (54, 170, 1), (55,), (55, 54, 1), (56,), (56, 231, 1), (57,),
         (57, 56, 1), (58,), (58, 56, 1), (59,), (59, 206, 1), (60,), (60, 59, 1), (61,), (61, 188, 1), (62,),
         (62, 61, 1), (63,), (63, 56, 1), (64,), (64, 229, 1), (65,), (65, 64, 1), (66,), (66, 223, 1), (67,),
         (67, 40, 1), (68,), (68, 2, 1), (68, 4, 1), (69,), (69, 66, 1), (70,), (70, 74, 1), (71,), (71, 65, 1), (72,),
         (72, 76, 1), (73,), (73, 66, 1), (74,), (74, 244, 1), (75,), (75, 78, 1), (76,), (76, 221, 1), (77,),
         (77, 66, 1), (78,), (78, 202, 1), (79,), (79, 85, 1), (80,), (80, 81, 1), (81,), (81, 204, 1), (82,),
         (82, 86, 1), (83,), (83, 66, 1), (84,), (84, 87, 1), (85,), (85, 220, 1), (86,), (86, 250, 1), (87,),
         (87, 248, 1), (88,), (88, 89, 1), (89,), (89, 251, 1), (90,), (90, 91, 1), (91,), (91, 186, 1), (92,),
         (92, 95, 1), (93,), (93, 94, 1), (94,), (94, 175, 1), (95,), (95, 180, 1), (96,), (96, 97, 1), (97,),
         (97, 209, 1), (98,), (98, 100, 1), (99,), (99, 102, 1), (100,), (100, 227, 1), (101,), (101, 106, 1), (102,),
         (102, 185, 1), (103,), (103, 107, 1), (104,), (104, 106, 1), (105,), (105, 109, 1), (106,), (106, 181, 1),
         (107,), (107, 135, 1), (108,), (108, 112, 1), (109,), (109, 224, 1), (110,), (110, 113, 1), (111,),
         (111, 47, 1), (112,), (112, 236, 1), (113,), (113, 190, 1), (114,), (114, 117, 1), (115,), (115, 116, 1),
         (116,), (116, 218, 1), (117,), (117, 183, 1), (118,), (118, 117, 1), (119,), (119, 120, 1), (120,),
         (120, 201, 1), (121,), (121, 122, 1), (122,), (122, 243, 1), (123,), (123, 127, 1), (124,), (124, 125, 1),
         (125,), (125, 197, 1), (126,), (126, 129, 1), (127,), (127, 217, 1), (128,), (128, 125, 1), (129,),
         (129, 68, 1), (130,), (130, 132, 1), (131,), (131, 136, 1), (132,), (132, 216, 1), (133,), (133, 117, 1),
         (134,), (134, 138, 1), (135,), (135, 46, 1), (135, 105, 1), (136,), (136, 173, 1), (137,), (137, 117, 1),
         (138,), (138, 191, 1), (139,), (139, 117, 1), (140,), (140, 141, 1), (141,), (141, 213, 1), (142,),
         (142, 141, 1), (143,), (143, 147, 1), (144,), (144, 15, 1), (145,), (145, 152, 1), (146,), (146, 154, 1),
         (146, 167, 1), (147,), (147, 141, 1), (148,), (148, 155, 1), (149,), (149, 141, 1), (150,), (150, 141, 1),
         (151,), (151, 141, 1), (152,), (152, 242, 1), (153,), (153, 157, 1), (154,), (154, 228, 1), (155,),
         (155, 195, 1), (156,), (156, 162, 1), (156, 163, 1), (157,), (157, 249, 1), (158,), (158, 159, 1), (159,),
         (159, 189, 1), (160,), (160, 161, 1), (161,), (161, 228, 1), (162,), (162, 0, 1), (163,), (163, 245, 1),
         (164,), (164, 165, 1), (165,), (165, 187, 1), (166,), (166, 57, 1), (167,), (167, 200, 1), (168,),
         (168, 214, 1), (169,), (169, 205, 1), (170,), (170, 60, 1), (170, 62, 1), (171,), (171, 177, 1), (172,),
         (172, 23, 1), (173,), (173, 137, 1), (174,), (174, 210, 1), (175,), (175, 44, 1), (175, 103, 1), (176,),
         (176, 118, 1), (177,), (177, 252, 1), (178,), (178, 179, 1), (179,), (179, 239, 1), (180,), (180, 96, 1),
         (181,), (181, 93, 1), (182,), (183,), (183, 146, 1), (184,), (184, 9, 1), (184, 20, 1), (185,), (185, 104, 1),
         (186,), (186, 134, 1), (186, 171, 1), (187,), (187, 169, 1), (188,), (188, 63, 1), (189,), (189, 160, 1),
         (190,), (190, 115, 1), (191,), (191, 139, 1), (192,), (193,), (193, 70, 1), (194,), (194, 42, 1), (195,),
         (195, 121, 1), (195, 123, 1), (196,), (196, 7, 1), (197,), (197, 126, 1), (198,), (198, 36, 1), (198, 38, 1),
         (199,), (199, 151, 1), (200,), (201,), (201, 148, 1), (202,), (202, 79, 1), (202, 82, 1), (203,),
         (203, 149, 1), (204,), (204, 83, 1), (205,), (205, 245, 1), (206,), (206, 58, 1), (207,), (207, 246, 1),
         (208,), (208, 207, 1), (209,), (209, 98, 1), (209, 99, 1), (210,), (210, 200, 1), (211,), (211, 11, 1),
         (211, 13, 1), (212,), (212, 142, 1), (213,), (213, 145, 1), (214,), (214, 176, 1), (215,), (215, 72, 1),
         (215, 75, 1), (216,), (216, 133, 1), (217,), (217, 128, 1), (218,), (218, 88, 1), (218, 168, 1), (219,),
         (219, 140, 1), (220,), (220, 77, 1), (221,), (221, 69, 1), (222,), (222, 25, 1), (222, 27, 1), (223,),
         (223, 92, 1), (224,), (224, 111, 1), (225,), (225, 18, 1), (226,), (226, 21, 1), (227,), (227, 101, 1), (228,),
         (228, 156, 1), (229,), (229, 32, 1), (229, 34, 1), (230,), (230, 48, 1), (231,), (231, 51, 1), (232,),
         (232, 119, 1), (233,), (233, 49, 1), (234,), (234, 16, 1), (235,), (235, 6, 1), (236,), (236, 90, 1),
         (236, 110, 1), (237,), (237, 150, 1), (238,), (238, 108, 1), (239,), (239, 130, 1), (239, 131, 1), (240,),
         (240, 29, 1), (241,), (241, 30, 1), (242,), (242, 153, 1), (243,), (243, 124, 1), (244,), (244, 53, 1),
         (244, 55, 1), (245,), (245, 208, 1), (246,), (246, 174, 1), (247,), (247, 41, 1), (248,), (248, 73, 1), (249,),
         (249, 158, 1), (250,), (250, 80, 1), (250, 84, 1), (251,), (251, 114, 1), (252,), (252, 178, 1)]
    g = Graph(from_list=L)
    return g
