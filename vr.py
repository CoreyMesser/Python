# string = 'PibblE kIbble obble'
# values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
# template = "Hi, I'm {name} and I love to eat {food}!"
# teachers_dict = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections', 'Python Basics'], 'Kenneth': ['Python', 'Collections']}
# it_a = ('def')
# it_b = ('abc')
# topics = {"conditions", "input"}
import datetime, pytz
from time import mktime
# from datetime import datetime
import doctest
#
# player = (0, 9, 10)
# direction = (0, 1)
# dt_str = '09/24/12 18:30'
# dt_strf = '%m/%d/%y %H:%M'
# tz_str = 'US/Pacific'
from flask import render_template

@app.route('/order', methods=('GET', 'POST'))
def order_lunch():
    return render_template('lunch.html', form=form)

class Treehouse(object):

    def email_hide(self):
        email = 'lucy@lucy.com'
        email_split = email.split('@')
        at_sy_index = 0
        for at_sy in email_split:
            if at_sy == '@':
                at_sy_index = email_split.index(at_sy)
                break
        email_list = [email_split[0], '***', "".join(email_split[at_sy_index::])]
        email_join = "".join(email_list)
        print(email_join)

if __name__ == '__main__':
    tr = Treehouse()
    tr.email_hide()

    # def average(self, num_list):
    #     """Return the average for a list of numbers
    #
    #     >>> num_list = [1, 2]
    #     1.5
    #
    #     """
    #     return sum(num_list) / len(num_list)

#
# def time_machine(self, num, str_dt):
#     starter = datetime.datetime(2015, 10, 21, 16, 29)
#     if str_dt == 'years'.lower:
#         num *= 365
#         str_dt = 'days'
#     return starter + eval('datetime.timedelta({}=num)'.format(str_dt))


# now = datetime.datetime.now()
# morning = now.replace(hour=9, minute=0)
# delta = datetime.timedelta(hours=5)
# messy = datetime.datetime.now().replace(hour=9, minute=0) + datetime.timedelta(days=1)
# today = datetime.datetime.combine(datetime.date.today(), datetime.time())
# datetime.timedelta.total_seconds()
# now.strftime('%B %d')
# now.strftime('%m/%d/%y')
#
# def to_string(self, dt):
#     dt1 = dt.strftime('%d %B %Y')
#     return dt1
#
# def from_string(self, dt_str, dt_strf):
#     dt3 = datetime.strptime(dt_str, dt_strf)
#     print(dt3.strftime(dt_strf))
#     return


# def minutes(self, dt1, dt2):
#     result1 = dt2 - dt1
#     result1.total_seconds()
#     print(result1)
#     # print(int((result1 + result2) / 60))
#     # return result.minutes
#
# def __init__(self, **kwargs):
#     self.hit_points = kwargs.get('hit_points', 1)
#     self.weapon = kwargs.get('weapon', 'sword')
#     self.color = kwargs.get('color', 'yellow')
#     self.sound = kwargs.get('sound', 'ROAR')
#
#
# # def __init__(self, hit_points=5, weapon='sword', color='yellow', sound='ROAR'):
# #     self.hit_points = hit_points
# #     self.weapon = weapon
# #     self.color = color
# #     self.sound = sound
#
# # hit_points = 1
# # color = 'yellow'
# # weapon = 'sword'
# # sound = 'roar'
#
# def battlecry(self):
#     return self.sound.upper()

#
# def tiler(self):
#     TILES = ('-', ' ', '-', ' ', '-', '||',
#          '_', '|', '_', '|', '_', '|', '||',
#          '&', ' ', '_', ' ', '||',
#          ' ', ' ', ' ', '^', ' ', '||'
#          )
#
#     for tile in TILES:
#         if tile == "||":
#             print(end="\n")
#         else:
#             print(tile, end="")

# def move(self, player, direction):
#     x, y, hp = player
#     a, b = direction
#
#     x = x + a
#     y = y + b
#
#     if x < 0 or x > 9:
#         hp = hp - 5
#         if x < 0:
#             x += 1
#         elif x > 9:
#             x += -1
#     if y < 0 or y > 9:
#         hp = hp - 5
#         if y < 0:
#             y += 1
#         elif y > 9:
#             y += -1
#     print(x, y, hp)
#     return x, y, hp

# COURSES = {
#     "Python Basics": {"Python", "functions", "variables",
#                       "booleans", "integers", "floats",
#                       "arrays", "strings", "exceptions",
#                       "conditions", "input", "loops"},
#     "Java Basics": {"Java", "strings", "variables",
#                     "input", "exceptions", "integers",
#                     "booleans", "loops"},
#     "PHP Basics": {"PHP", "variables", "conditions",
#                    "integers", "floats", "strings",
#                    "booleans", "HTML"},
#     "Ruby Basics": {"Ruby", "strings", "floats",
#                     "integers", "conditions",
#                     "functions", "input"}
# }
#
# def covers(self, topics):
#     list_course = []
#     for key in self.COURSES:
#         value_set = self.COURSES[key]
#         new_set = value_set.intersection(topics)
#         if len(new_set) > 0:
#             list_course.append(key)
#             print(list_course)
#     return list_course
#
# def covers_all(self, topics):
#     course_list = []
#     for key in self.COURSES:
#         value_set = self.COURSES[key]
#         new_set = value_set.intersection(topics)
#         if len(new_set) >= 2:
#             course_list.append(key)
#     print(course_list)
#     return course_list

# def combo(self, it_a, it_b):
#     i_l = []
#     i_m = []
#     itter = [it_a, it_b]
#     for items in itter:
#         i_l.append(tuple(items))
#     for item_s in i_l:
#         if i_l.index(item_s) == 0:
#             for item_ss in item_s:
#                 i_m.append(item_ss)
#         else:
#             in_out, in_in = 0, 1
#             for item_ss in item_s:
#                 i_m.insert(in_in, item_ss)
#                 a = i_m[in_out: in_in+1]
#                 del i_m[in_out: in_in+1]
#                 i_m.append(tuple(a))
#     print(i_m)
#
#     return i_m

# def combo(self, itter, atter):
#     i_l = []
#     i_m = []
#     for items in itter:
#         i_l.append(tuple(items))
#     for item_s in i_l:
#         item_len = len(item_s)
#         if i_l.index(item_s) == 0:
#             for item_ss in item_s:
#                 i_m.append(item_ss)
#         else:
#             in_out, in_in = 0, 1
#             for item_ss in item_s:
#                 i_m.insert(in_in, item_ss)
#                 a = i_m[in_out: in_in+1]
#                 del i_m[in_out: in_in+1]
#                 i_m.append(tuple(a))
#     i_m = tuple(i_m)
#     return i_m

# def stringcases(self, string):
#     string_s = (string.lower(), string.upper(), string.title(), "".join(list(string[::-1])))
#     print(string_s)

# def multi(self, base, *nums):
#     total = base
#     for a in nums:
#         total *= a
#     print(total)
#     return total

# def num_teachers(self, teachers_dict):
#     num_teach = len(teachers_dict.keys())
#     print(num_teach)
#     return num_teach
#
# def num_courses(self, teachers_dict):
#     b = 0
#     for values in teachers_dict.keys():
#         a = len(teachers_dict[values])
#         b = b + a
#     print(b)
#     return b
#
# def courses(self, teachers_dict):
#     course_list = []
#     for values in teachers_dict.values():
#         for value in values:
#             course_list.append(value)
#     print(course_list)
#     return course_list
#
# def most_courses(self, teachers_dict):
#     b = 0
#     for values in teachers_dict.keys():
#         a = len(teachers_dict[values])
#         if a > b:
#             c = values
#             b = a
#     print(c)
#     return c
#
# def stats(self, teachers_dict):
#     stats_l = []
#     for teacher in teachers_dict.keys():
#         courses = len(teachers_dict[teacher])
#         teacher_s = [teacher, courses]
#         stats_l.append(teacher_s)
#     print(stats_l)
#     return stats_l


# def string_factory(self, values, template):
#     new_l = []
#     for dict in values:
#         new_l.append(template.format(**dict))
#     print(new_l)


#     def disemvowel(self, word):
#         vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         word_l = list(word)
#         for a in word_l[::-1]:
#             if a in vowel:
#                 word_l.pop(word_l.index(a))
#         word_y = "".join(word_l)
#         print(word_y)
#         return word_y