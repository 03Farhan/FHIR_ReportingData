import matplotlib.pyplot as plt
import requests


def marital_status():
    data = requests.get('http://127.0.0.1:5002/marital_statuses').json()
    labels = data.keys()
    sizes = []
    for label in labels:
        sizes.append(data[label])
    colors = ['gold', 'yellowgreen']
    explode = (0.1, 0) 

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.title("Marital Status of Patients")
    plt.axis('equal')
    plt.savefig('MaritalStatus.png')
    plt.cla()

def birth_decades():
    labels = []
    data_male = requests.get('http://127.0.0.1:5002/birth_decades_male').json()
    data_female = requests.get('http://127.0.0.1:5002/birth_decades_female').json()

    for decade in data_male.keys():
        labels.append(decade)
    for decade in data_female.keys():
        if decade not in labels:
            labels.append(decade)

    labels.sort()
    male_means = []
    female_means = []

    for decade in labels:
        male_means.append(data_male[decade])
        female_means.append(data_female[decade])

    width = 0.35       
    fig, ax = plt.subplots()
    plt.bar(labels, male_means, width, label='Men')
    plt.bar(labels, female_means, width, bottom=male_means, label='Women')

    plt.ylabel('Number of Patient Births')
    plt.xlabel('Decade')
    plt.title('Number of Patient Births in Each Decade')
    plt.legend()
    plt.savefig("BirthDecades.png")
    plt.cla()



def languages():
    data = requests.get('http://127.0.0.1:5002/languages').json()
    labels = []
    for lang in data.keys():
        labels.append(lang)

    values = []
    for lang in labels:
        values.append(data[lang])

    quick_sort(values, labels)
    labels = labels[:5]
    values = values[:5]

    plt.bar(labels, values, align='center', alpha=0.5)
    plt.ylabel('Number of Patients')
    plt.xlabel('Language')
    plt.title('Top 5 Languages Spoken by Patients')
    plt.savefig("Languages.png")
    plt.cla()
    

def partition(array, begin, end, array2):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] >= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
            array2[i], array2[pivot_idx] = array2[pivot_idx], array2[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    array2[pivot_idx], array2[begin] = array2[begin], array2[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end, array2):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end, array2)
    quick_sort_recursion(array, begin, pivot_idx-1, array2)
    quick_sort_recursion(array, pivot_idx+1, end, array2)

def quick_sort(array, array2, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end, array2)

marital_status()
birth_decades()
languages()


