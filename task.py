import os
from requests import get
import json
import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Task(object):
    def __init__(self):
        self.response = get('http://db.cs.pitt.edu/courses/cs1656/data/hours.json', verify=False)
        self.hours = json.loads(self.response.content)

    def part4(self):
        data_hours = open('hours.csv', 'w', newline='')
        writer = csv.writer(data_hours)
        count = 0
        for data in self.hours:
            if count ==0:
                writer.writerow(['name', 'day', 'time'])
                count +=1
            writer.writerow(data.values())
        data_hours.close()

    def part5(self):
        #write output to 'part5.txt'
        r = open('hours.csv', 'r')
        f = open('part5.txt', 'w')
        for data in r:
            f.write(data)
        r.close()
        f.close()

    def part6(self):
        #write output to 'part6.txt'
        f = open('part6.txt', 'w')
        with open('hours.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                f.write("['")
                f.write("', '".join(row))
                f.write("']")
        f.close()
        csvfile.close()

    def part7(self):
        #write output to 'part7.txt'
        f = open('part7.txt', 'w')
        with open('hours.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for data in row:
                    f.write(data)



if __name__ == '__main__':
    task = Task()
    task.part4()
    task.part5()
    task.part6()
    task.part7()
