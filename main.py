#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 12:08:19 2023
@author: kilin(Alan Weng)
@purpose: view/edit/visualize a csv file
"""
import pandas, csv, numpy
import matplotlib.pyplot as plt


def save_csv(filename, fields, rows):   
    csvfile = open(filename, "w")
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)  
    csvwriter.writerows(rows) 

def add_entry(rows):
    date = ""
    date += input("What is the month?: ")+"/"
    date += input("What is the day?: ")+"/"
    date += input("What is the year (xxxx)?: ")
    type_amount = "Expense"
    money_amount = "$"+"{:.2f}".format(float(\
                                    input("Input a monetary value: ")))
    category = input("What is the category?: ").lower().title()
    rows.append([date,type_amount,money_amount,category])
    return rows
    
    


if __name__ == "__main__":
    # ------------
    # Intro
    # ------------
    print("Hello, this is a program to edit your csv file named data.csv")
    while True:
        df = pandas.read_csv("data.csv")
        # names of fields
        fields = ["Date","Type","Amount","Description"]
        # get data from each row, put in list and then in a big list
        rows = []
        for index in range(len(df)):
            row = []
            for field in fields:
                row.append(df[field][index])
            rows.append(row)
        print("-------------------------------")
        print(" 1 - View your csv")
        print(" 2 - Add a entry")
        print(" 3 - Delete a entry")
        print(" 4 - Visualize your expenses")
        print(" 5 - Exit")
        print("-------------------------------")
        
        choice = int(input("What is your choice?: "))
        print("-------------------------------")
        # ------------
        # Menu
        # ------------
        if choice == 1:
            print(df)
        elif choice == 2:
            rows = add_entry(rows)
            save_csv("data.csv", fields, rows)
        elif choice == 3:
            print(df)
            print("-------------------------------")
            d_entry = int(input("Which one (0 - {})?: ".format(len(rows)-1)))
            print("-------------------------------")
            rows.pop(d_entry)
            save_csv("data.csv", fields, rows)
            print("------------Deleted!-----------")
        elif choice == 4:
            # this is to  find all the categories
            categories = set()
            for row in rows:
                categories.add(row[3])
            categories = list(categories)
            categories.sort()
            # this is to get values of each indicies
            cat_values = []
            for category in categories:
                cat_val = 0.0
                for row in rows:
                    if row[3] == category:
                        cat_val += float(row[2].replace("$","").replace(",",""))
                cat_values.append(cat_val)
            m_expl = []
            for category in categories:
                m_expl.append(.05)
            plt.barh(numpy.array(categories), numpy.array(cat_values))
            plt.show()
            plt.pie(numpy.array(cat_values), labels = categories, \
                    explode = m_expl, shadow = True, startangle = 90)
            plt.show() 
        elif choice == 5:
            break




