import unittest
from minion_assign import answer


class IDGenerator(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    known_values = ((1211, 10, 1),
                    (210022, 3, 3))

    id_ls = []
    base_s = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    id_cycle0 = []
    id_cycle1 = []
    id_cycle2 = []
    id_cycle3 = []
    id_cycle4 = []
    id_cycle5 = []
    id_cycle6 = []
    id_cycle7 = []
    id_cycle8 = []
    id_cycle9 = []
    id_cycle10 = []

    id_s = 1000
    while id_s < 10000:
        id_ls.append(id_s)
        id_s += 1

    def test_id_cycler(self):
        for m_id in IDGenerator.id_ls:
            for b_id in IDGenerator.base_s:
                min_cycle = answer(m_id, b_id)
                if min_cycle == 0:
                    IDGenerator.id_cycle0.append([min_cycle, m_id, b_id])
                if min_cycle == 1:
                    IDGenerator.id_cycle1.append([min_cycle, m_id, b_id])
                    #IDGenerator.id_cycle1.update({min_cycle: [m_id, b_id]})
                elif min_cycle == 2:
                    IDGenerator.id_cycle2.append([min_cycle, m_id, b_id])
                elif min_cycle == 3:
                    IDGenerator.id_cycle3.append([min_cycle, m_id, b_id])
                elif min_cycle == 4:
                    IDGenerator.id_cycle4.append([min_cycle, m_id, b_id])
                elif min_cycle == 5:
                    IDGenerator.id_cycle5.append([min_cycle, m_id, b_id])
                elif min_cycle == 6:
                    IDGenerator.id_cycle6.append([min_cycle, m_id, b_id])
                elif min_cycle == 7:
                    IDGenerator.id_cycle7.append([min_cycle, m_id, b_id])
                elif min_cycle == 8:
                    IDGenerator.id_cycle8.append([min_cycle, m_id, b_id])
                elif min_cycle == 9:
                    IDGenerator.id_cycle9.append([min_cycle, m_id, b_id])
                elif min_cycle == 10:
                    IDGenerator.id_cycle10.append([min_cycle, m_id, b_id])
                # else:
                #     pass

        for key, val in IDGenerator.id_cycle2:
            print(key, ">>", val)

if __name__ == '__main__':

    unittest.main()
