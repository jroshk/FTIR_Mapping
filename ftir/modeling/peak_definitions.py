"""
Peak definitions based on literature values

This file provides peak definitions based on different literature sources. The
source of the definition is provides in the comments of this file, and the
name of the definition follows the same convention:
    firstauthor_solvent_year

The peak definitions are dictionary objects with four items

means: List
    list of the mean frequencies for a given peak

uncertainties: List of tuples
    list of tuples providing to lower and upper bounds of the absorbance band

relative_uncertainties : List
    list of the plus/minus values around the mean. The `relative_uncertainties`
    are used to calculate the `uncertainties`.

assignments : List
    list of the literature peak assignments

"""
four_peak = {
    'means': [1627, 1650, 1679,1700],
    'uncertainties': [(1616, 1637), (1638, 1662), (1663, 1696), (1697, 1703)],
    #'relative_uncertainties': [10, 12, 16,3],
    'relative_uncertainties': [2, 2, 2,2],
    'assignments': ['aggregate \u03B2-strand/\u03B2-sheet',
                    'random coils + \u03B1 helices', '\u03B2-turns', 'intermolecular \u03B2-sheets (weak)']
}

# Dong et. al., Biochemistry. 1990
dong_h2o_1990 = {
    'means': [1624, 1627, 1632, 1638, 1642, 1650, 1656, 1666, 1672, 1680,
              1688],
    'uncertainties': [(1623.5, 1624.5), (1626, 1628), (1631, 1633),
                      (1637, 1639), (1641, 1643), (1649, 1651), (1654, 1658),
                      (1665, 1667), (1671, 1673), (1679, 1681), (1687, 1689)],
    'relative_uncertainties': [0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    'assignments': ['beta_sheet', 'beta_sheet',
                    'beta_sheet_and_extended_chain', 'beta_sheet', 'unordered',
                    'alpha_helix', 'turn', 'turn', 'turn', 'turn']
}


# Yang et. al., Nature Protocols. 2015
yang_h20_2015 = {
    'means': [1624, 1627, 1633, 1638, 1642, 1648, 1656, 1663, 1667, 1675, 1680,
              1685, 1691, 1696],
    'uncertainties': [(1623, 1625), (1625, 1629), (1631, 1635), (1636, 1640),
                      (1641, 1643), (1646, 1650), (1654, 1658), (1660, 1666),
                      (1666, 1668), (1674, 1676), (1678, 1682), (1683, 1687),
                      (1689, 1693), (1694, 1698)],
    'relative_uncertainties': [1, 2, 2, 2, 1, 2, 2, 3, 1, 1, 2, 2, 2, 2],
    'assignments': ['\u03B2-sheet', '\u03B2-sheet', '\u03B2-sheet', '\u03B2-sheet',
                    '\u03B2-sheet', 'unordered', '\u03B1-helix', '310-helix',
                    '\u03B2-turn', '\u03B2-turn', '\u03B2-turn', '\u03B2-turn',
                    '\u03B2-sheet', '\u03B2-sheet']
}


yang_d20_2015 = {
    'means': [1624, 1631, 1637, 1641, 1645, 1653, 1663, 1671, 1675, 1683, 1689,
              1694],
    'uncertainties': [(1620, 1628), (1628, 1634), (1634, 1640), (1639, 1643),
                      (1641, 1649), (1649, 1657), (1659, 1667), (1668, 1674),
                      (1670, 1680), (1681, 1685), (1687, 1691), (1692, 1696)],
    'relative_uncertainties': [4, 3, 3, 2, 4, 4, 4, 3, 5, 2, 2, 2],
    'assignments': ['beta_sheet', 'beta_sheet', 'beta_sheet', '310_helix',
                    'unordered', 'alpha_helix', 'beta_turn', 'beta_turn',
                    'beta_sheet', 'beta_turn', 'beta_turn', 'beta_turn']
}


#, added by jeff, modify this from "Determining Beta-Sheet Crystallinity in Fibrous Proteins by Thermal Analysis and Infrared Spectroscopy" https://pubs.acs.org/doi/full/10.1021/ma0610109
hu_Kaplan_Cebe_2006_actual = {
    'means': [1610, 1618.5, 1624.5, 1632.5,  1642, 1651, 1659, 1666.5, 1678, 1691, 1700],
    'uncertainties': [(1605, 1615), (1616, 1621), (1622, 1627), (1628, 1637),
                      (1638, 1646), (1647, 1655), (1656, 1662), (1663, 1670),
                      (1671, 1685), (1686, 1696), (1697, 1703)],
    'relative_uncertainties': [5, 2.5, 2.5, 4.5, 4, 4, 3, 3.5, 7, 5, 3],
    'assignments': ['(Tyr) side chains/aggregate strands', 'aggregate beta-strand/beta_sheet(weak)', 
                    'intermolecular beta_sheet (strong)', 'intramolecular beta_sheet (strong)^b',
                    'random coils/extended', 'random coils', 'alpha-helices', 'turns',
                    'turns', 'turns', 'intermolecular beta_sheets (weak)']
}

#local Cebe reference list - maybe try to subtract water from a film and see how it looks?
hu_Kaplan_Cebe_2006_modified = {
    'means': [1610, 1619, 1625, 1632,  1642, 1652, 1659, 1666, 1679, 1692, 1700],
    'uncertainties': [(1605, 1615), (1616, 1621), (1622,1627),(1628, 1637), (1638, 1646),
                      (1647, 1655), (1656, 1662), (1663, 1670), (1671, 1685),
                      (1686, 1696), (1697, 1703)],
    'relative_uncertainties': [5, 2.5, 2.5, 4.5, 4, 4, 3, 3.5, 7, 5, 3],
    'assignments': ['(Tyr) side chains/aggregate strands', 'aggregate beta-strand/beta_sheet(weak)', 
                    'intermolecular beta_sheet (strong)', 'intramolecular beta_sheet (strong)^b',
                    'random coils/extended', 'random coils', 'alpha-helices', 'turns',
                    'turns', 'turns', 'intermolecular beta_sheets (weak)']
}


#from ftir.modeling.peak_definitions import hu_Kaplan_Cebe_2006_actual
hu_Kaplan_Cebe_2006_rounded = {
    'means': [1610, 1619, 1625, 1633,  1642, 1650, 1659, 1667, 1679, 1692, 1700],
    'uncertainties': [(1605, 1615), (1616, 1621), (1622, 1627), (1628, 1637),
                      (1638, 1646), (1647, 1655), (1656, 1662), (1663, 1670),
                      (1671, 1685), (1686, 1696), (1697, 1703)],
    'relative_uncertainties': [5, 2.5, 2.5, 4.5, 4, 4, 3, 3.5, 7, 5, 3],
    'assignments': ['(Tyr) side chains/aggregate strands', 'aggregate \u03B2-strand/\u03B2-sheet(weak)', 
                    'intermolecular \u03B2-sheet (strong)', 'intramolecular \u03B2-sheet (strong)^b',
                    'random coils/extended', 'random coils', '\u03B1-helices', 'turns',
                    'turns', 'turns', 'intermolecular \u03B2_sheets (weak)']
}





five_peak = {
    'means': [1627,1651,1659, 1679,1700],
    'uncertainties': [(1616, 1637), (1638, 1655),(1656, 1662), (1663, 1696), (1697, 1703)],
    #'relative_uncertainties': [10, 12, 16,3],
    'relative_uncertainties': [2,2,2,2,2],
    'assignments': ['aggregate \u03B2-strand/\u03B2-sheet',
                    'random coils',' \u03B1-helices', '\u03B2-turns', 'intermolecular \u03B2-sheets (weak)']
}

five_peakv2 = {
    'means': [1610, 1627, 1650, 1679,1700],
    'uncertainties': [(1605,1615),(1620, 1633), (1640, 1660), (1663, 1696), (1697, 1703)],
    'relative_uncertainties': [5,5, 5, 5,5],
    # 'uncertainties': [(1605,1615),(1616, 1637), (1638, 1662), (1663, 1696), (1697, 1703)],
    # 'relative_uncertainties': [5,5, 5, 5,5],
    'assignments': ['side-chains', 'aggregate \u03B2-strand/\u03B2-sheet',
                    'random coils + \u03B1 helices', '\u03B2-turns', 'intermolecular \u03B2-sheets (weak)']
}

six_peak = {
    'means': [1610, 1625,  1646, 1659, 1679, 1700],
    'uncertainties': [(1605, 1615), (1616, 1637),
                      (1638, 1646), (1647, 1662), (1663, 1696), (1697, 1703)],
    'relative_uncertainties': [5, 10.5, 4, 7.5, 16.5, 3],
    'assignments': ['(Tyr) side chains/aggregate strands', 'aggregate beta-strand/beta_sheet',
                    'random coils', '\u03B1-helices', 'turns', 'intermolecular beta_sheets (weak)']
}

# six_peakv2 = {
#     'means': [1610, 1627, 1646, 1659, 1679,1700],
#     'uncertainties': [(1605,1615),(1620, 1637), (1638,1655), (1656,1662), (1663, 1696), (1697, 1703)],
#     'relative_uncertainties': [reluncert,reluncert,reluncert,reluncert,reluncert,reluncert],
#     # 'uncertainties': [(1605,1615),(1616, 1637), (1638, 1662), (1663, 1696), (1697, 1703)],
#     # 'relative_uncertainties': [5,5, 5, 5,5],
#     'assignments': ['side-chains', 'aggregate \u03B2-strand/\u03B2-sheet',
#                     'random coils', '\u03B1 helices', '\u03B2-turns', 'intermolecular \u03B2-sheets (weak)']
# }
four_peak = {
    #used up until 1.22.2024, but needed to try IPA screening  settings from 3.2023
    # 'means': [1620,  1636, 1679, 1700],
    'means': [1627,  1650, 1679,1700],

    #    #used up until 1.22.2024, but needed to try IPA screening  settings from 3.2023
    # 'uncertainties': [(1613, 1626), (1627, 1664), (1668, 1685), (1697, 1703)],
    'uncertainties': [(1613, 1632), (1640, 1657), (1668, 1685), (1697, 1703)],
    # 'relative_uncertainties': [10, 12, 16,3],
    # 'relative_uncertainties': [2, 2, 1,2],
    'assignments': ['aggregate \u03B2-strand/\u03B2-sheet',
                    'random coils + \u03B1 helices', '\u03B2-turns', 'intermolecular \u03B2-sheets (weak)']}

four_peak_2024_1_26 = {

    # 'means': [1620,  1636, 1679, 1700],
    'means': [1624,  1638, 1679,1700],

    # 'uncertainties': [(1613, 1626), (1627, 1664), (1668, 1685), (1697, 1703)],
    'uncertainties': [(1613, 1630), (1631, 1657), (1668, 1685), (1697, 1703)],
    # 'relative_uncertainties': [2, 2, 1,2],
    'assignments': ['aggregate \u03B2-strand/\u03B2-sheet',
                    'random coils + \u03B1 helices', '\u03B2-turns', 'intermolecular \u03B2-sheets (weak)']}

four_peak_2023_3_15_IPAScreening_Samba = {


    'means': [1627,  1650, 1679,1700],
    'uncertainties': [(1613, 1629), (1634, 1664), (1668, 1685), (1697, 1703)],
    'relative_uncertainties': [5, 2.5, 2.5, 4.5, 4, 4, 3, 3.5, 7, 5, 3],
    'assignments': ['aggregate \u03B2-strand/\u03B2-sheet',
                    'random coils + \u03B1 helices', '\u03B2-turns', 'intermolecular \u03B2-sheets (weak)']}

four_peak_2024_MeOH = {
    'means': [1625, 1637, 1679, 1700], 
    'uncertainties': [(1613, 1626), (1632, 1642), (1668, 1685), (1697, 1703)], 
    'assignments': ['aggregate β-strand/β-sheet', 'random coils + α helices', 'β-turns', 'intermolecular β-sheets (weak)']}
