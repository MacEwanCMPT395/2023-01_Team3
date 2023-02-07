# Honestly each part of these should have their own CSV file.

# A file for Programs
# A file for Courses
# A file for populations

# Then we can import it here, skip the dictionaries and
# create the classes immediately.
# This way we can also check for missing classes and
# other missing info and ask the user if they want to fill it in.

programinfo = {
    "PCOM":{
        "Term":{
            1:{"Population":210,
               "Classes":["PCOM 0101",
                          "PCOM 0105",
                          "PCOM 0107",
                          "CMSK 0233",
                          "CMSK 0235"]
               },
            2:{"Population":133,
               "Classes":["PCOM 0102",
                          "PCOM 0201",
                          "PCOM 0108"]
               },
            3:{"Population":64,
               "Classes":["PCOM 0202",
                          "PCOM 0103",
                          "PCOM 0109"]
               }
        }
    }
}
# 24 hour time scale for classes
courses ={"PCOM 0101":{"Name":"Business Writing I",
                           "Hours":35,
                           "Duration": 1.5,
                           "MinTime":8,
                           "Maxtime":17,
                           "Lab":False},
             "PCOM 0105":{"Name":"Intercultural Communication Skills",
                           "Hours":35,
                           "Duration": 1.5,
                           "MinTime":8,
                           "Maxtime":17,
                           "Lab":False},
             "PCOM 0107":{"Name":"Technical Development I: \
Microsoft Word, Excel and Power Point",
                           "Hours":18,
                           "Duration": 1.5,
                           "Min":8,
                           "Max":17,
                           "Lab":True},
             "CMSK 0233":{"Name":"MS Project Essentials",
                           "Hours":7,
                           "Duration": 1.5,
                           "MinTime":8,
                           "Maxtime":17,
                           "Lab":True},
             "CMSK 0235":{"Name":"MS Visio Essentials",
                           "Hours":7,
                           "Duration": 1.5,
                           "MinTime":8,
                           "Maxtime":17,
                           "Lab":True},
}
