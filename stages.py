# Work on project. Stage 5/7: Information gain
import math

H_data = math.log(5, 2) / 5 + math.log(5/2, 2) * 2/5 + math.log(5/2, 2) * 2/5
H_g1 = math.log(2, 2) / 2 + math.log(2, 2) / 2
H_g2 = math.log(3/2, 2) * 2/3 + math.log(3, 2) / 3
H_g3 = math.log(3/2, 2) * 2/3 + math.log(3, 2) / 3
H_g4 = math.log(1, 2) + math.log(1, 2)

IG_1 = H_data - H_g1 / 2 - H_g2 / 2
IG_2 = H_data - H_g3 * 3/5 - H_g4 * 2/5

print('H(dataset) =', H_data, '\nH(group1) =', H_g1, '\nH(group2) =', H_g2,
      '\nH(group3) =', H_g3, '\nH(group4) =', H_g4,
      '\n\nIG(split1) =', IG_1, '\nIG(split2) =', IG_2)


# Work on project. Stage 6/7: Build a decision tree with information gain
print('\n\n| Petal width | Sepal width |  Color |     Species     |',
      '\n|     0.2     |     3.5 	| purple | Iris Setosa     |',
      '\n|     1.5	  |     2.1 	| purple | Iris Versicolor |',
      '\n|     1.4	  |     2.2	    | purple | Iris Versicolor |',
      '\n|     1.5	  |     2.2	    | yellow | Iris Virginica  |')
species = math.log(4, 2) / 4 + math.log(4/2, 2) / 4 * 2 + math.log(4, 2) / 4
print('\nH(Species) =', species)

print('\nIs the petal width less or equal to 0.2?')
IG_petal_1_1 = species - math.log(1, 2) / 4 - (math.log(3/2, 2) * 2/3 + math.log(3, 2) / 3) * 3/4
print('Firs split IG(petal<=0.2) =', IG_petal_1_1)

print('\nIs the petal width less or equal to 1.4?')
IG_petal_1_2 = species - (math.log(2, 2) / 2 + math.log(2, 2) / 2) * 2/4 - (math.log(2, 2) / 2 + math.log(2, 2) / 2) * 2/4
print('Firs split IG(petal<=1.4) =', IG_petal_1_2)

print('\nIs the sepal width less or equal to 2.1?')
IG_sepal_1_1 = species - math.log(1, 2) / 4 - (math.log(3, 2) / 3 + math.log(3, 2) / 3 + math.log(3, 2) / 3) * 3/4
print('Firs split IG(sepal<=2.1) =', IG_sepal_1_1)

print('\nIs the sepal width less or equal to 2.2?')
IG_sepal_1_2 = species - (math.log(3/2, 2) * 2/3 + math.log(3, 2) / 3) * 3/4 - math.log(1, 2) / 4
print('Firs split IG(sepal<=2.2) =', IG_sepal_1_2)

print('\nIs the color blue?')
IG_blue_1 = None
print('Firs split IG(blue) =', IG_blue_1)

print('\nIs the color purple?')
IG_purple_1 = species - (math.log(3, 2) / 3 + math.log(3/2, 2) * 2/3) * 3/4 - math.log(1, 2) / 4
print('Firs split IG(purple) =', IG_purple_1)

print('\nIs the color yellow?')
IG_yellow_1 = species - math.log(1, 2) / 4 - (math.log(3, 2) / 3 + math.log(3/2, 2) * 2/3) * 3/4
print('Firs split IG(yellow) =', IG_yellow_1)

H_petal_0_2 = math.log(3/2, 2) * 2/3 + math.log(3, 2) / 3
print('\n\n| Sepal width |  Color |     Species     |',
      '\n|     2.1 	  | purple | Iris Versicolor |',
      '\n|     2.2	  | purple | Iris Versicolor |',
      '\n|     2.2	  | yellow | Iris Virginica  |',
      '\n\nH((petal>=0.2) =', H_petal_0_2)

print('\nIs the sepal width less or equal to 2.1?')
IG_sepal_2_1 = H_petal_0_2 - math.log(1, 2) - (math.log(2, 2) / 2 + math.log(2, 2) / 2) * 2/3
print('Second split IG(sepal<=2.1) =', IG_sepal_2_1)

print('\nIs the sepal width less or equal to 2.2?')
IG_sepal_2_2 = H_petal_0_2 - H_petal_0_2
print('Second split IG(sepal<=2.2) =', IG_sepal_2_2)

print('\nIs the color blue?')
IG_blue_2 = None
print('Second split IG(blue) =', IG_blue_2)

print('\nIs the color purple?')
IG_purple_2 = H_petal_0_2 - math.log(1, 2) - math.log(1, 2)
print('Second split IG(purple) =', IG_purple_2)

print('\nIs the color yellow?')
IG_yellow_2 = H_petal_0_2 - math.log(1, 2) - math.log(1, 2)
print('Second split IG(yellow) =', IG_yellow_2)
