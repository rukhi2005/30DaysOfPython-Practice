# Exercises: Day 5

#1.
list = []

#2.
names = ['Mike', 'Will', 'Lucas', 'Dustin', 'Eleven', 'Steve', 'Nancy', 'Jonathan', 'Max']

#3.
print(len(names))

#4.
print(names[0])
print(names[4])
print(names[-1])

#5.
mixed_data_types = ['Rukhaiya', 20, 152, 'Unmarried', 'Toronto, Canada']

#6.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7.
print(it_companies)

#8.
print("No: of companies: ", len(it_companies))

#9.
print(it_companies[0])
print(it_companies[2])
print(it_companies[-1])

#10.
it_companies[2] = 'Visa'

#11.
it_companies.append('Stripe')

#12.
it_companies.insert(4, 'Pintrest')
print(it_companies)

#13.
it_companies[1] = it_companies[1].upper()
print(it_companies)

#14.
print('# '.join(it_companies))

#15.
does_exist = 'Pintrest' in it_companies
print(does_exist)

#16.
it_companies.sort()
print(it_companies)

#17.
it_companies.sort(reverse=True)
print(it_companies)

#18.
print(it_companies[:3])

#19.
print(it_companies[-3:])

#20.
print(it_companies[4:5])

#21.
it_companies.pop(0)
print(it_companies)

#22.
it_companies.pop(3)

#23
it_companies.pop(6)

#24.
it_companies.clear()

#25.
del it_companies

#26.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
list = front_end + back_end
print(list)

#27.
full_stack = list.copy()
print(full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQl')
print(full_stack)

#Exercises: Level 2

#1.
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
print(min_age)
max_age = max(ages)
print(max_age)
ages.append(min_age)
ages.append(max_age)

mid = len(ages) // 2
median = (ages[mid] + ages[mid - 1]) / 2
print(median)

average = sum(ages) / len(ages)
print(average)

age_range = max_age - min_age
print(age_range)

diff_min = abs(min_age - average)
diff_max = abs(max_age - average)
print("abs(min - average):", diff_min)
print("abs(max - average):", diff_max)

#2.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

countries_count = len(countries)

middle = (countries_count + 1) // 2   # ensures first half gets extra if odd

first_half = countries[:middle]
second_half = countries[middle:]

print("First half:", first_half)
print("Second half:", second_half)
print("First half length:", len(first_half))
print("Second half length:", len(second_half))

#3.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first, second, third, *scandic = countries

print("First country:", first)
print("Second country:", second)
print("Third country:", third)
print("Scandic countries:", scandic)
