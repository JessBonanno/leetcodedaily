"""
*** Financial Crisis ***
------------------------
Once upon a time, in a kingdom far, far away, there lived a King Byteasar IV. His kingdom in the middle of a financial crisis, Byteasar was struggling to keep the economy out of a recession. Unfortunately there was not much he could do, and after much agonizing he came to the only solution: one of his cities had to be demolished, since keeping communication active between all the cities is way too expensive.

It is not yet known if Byteasar chose a city to destroy after careful planning or picked one at random. As a person with a PhD in History and Nobel prize in Computer Science, you can solve this mystery! Archaeologists have recently found a manuscript with information about the roads between the cities, that is now stored in the roadRegister matrix. You want to try and remove each city one by one and compare the road registers obtained this way. Thus you'll be able to compare the obtained roads and determine whether the one picked by Byteasar was the best by some criteria.

Given the roadRegister, return an array of all the road registers obtained after removing each of the cities one by one.

Example

For

roadRegister = [[false, true,  true,  false],
                [true,  false, true,  false],
                [true,  true,  false, true ],
                [false, false, true,  false]]
the output should be

financialCrisis(roadRegister) = [
  [[false, true,  false],
   [true,  false, true ],
   [false, true,  false]],
  [[false, true,  false],
   [true,  false, true ],
   [false, true,  false]],
  [[false, true,  false],
   [true,  false, false],
   [false, false, false]],
  [[false, true,  true ],
   [true,  false, true ],
   [true,  true,  false]]
]
"""

roadRegister = [[False, False, False, False, True, False],
                [False, False, True, False, True, False],
                [False, True, False, True, True, True],
                [False, False, True, False, False, False],
                [True, True, True, False, False, True],
                [False, False, True, False, True, False]]


def financialCrisis(roadRegister):

    # the results will contain a copy of the matrix reflecting each city
    # removed one at a time
    # create result array to hold final result
    result = []

    # helper function to remove the current city
    def remove_city(current_city):
        # print(roadRegister[current_city + 1:])
        new_road_register = []
        for i in range(len(roadRegister)):
            if roadRegister[i] != roadRegister[current_city]:
                new_road_register.append(roadRegister[i])
        return new_road_register

    # helper function to remove the roads of removed city
    def remove_roads(city, road_to_remove):
        # if the road is not the road to remove save it in new array
        kept_roads = []
        for i in range(len(city)):
            if i != road_to_remove:
                kept_roads.append(city[i])
        return kept_roads

    # iterate the matrix

    for city in range(len(roadRegister)):
        new_register = []
        # remove the city array
        temp_road_register = (remove_city(city))
        # remove the road element of each other array
        for i in range(len(temp_road_register)):
            # add that to the result matrix
            new_register.append(remove_roads(temp_road_register[i], city))
        print('new register', new_register)
        result.append(new_register)

    # return result



"""
def financialCrisis(roadRegister):
    newRegister = []
    n = len(roadRegister)
    newRegister = [ [ [roadRegister[j][k] for j in range(n) if j!=l] for k in range(n) if k!=l] for l in range(n)] 
    return newRegister

11:34
def financialCrisis(r):
    return [[v[:j] + v[j+1:] for i, v in enumerate(r) if i!=j] for j in range(len(r))]
"""
print(financialCrisis(roadRegister))

# not sure why the expected output only wants 4 registers returned when the
# accepted output
# [[[false,true,false,true,false],[true,false,true,true,true],[false,true,false,false,false],[true,true,false,false,true],[false,true,false,true,false]],
#  [[false,false,false,true,false],[false,false,true,true,true],[false,true,false,false,false],[true,true,false,false,true],[false,true,false,true,false]],
#  [[false,false,false,true,false],[false,false,false,true,false],[false,false,false,false,false],[true,true,false,false,true],[false,false,false,true,false]],
#  [[false,false,false,true,false],[false,false,true,true,false],[false,true,false,true,true],[true,true,true,false,true],[false,false,true,true,false]],
#  [[false,false,false,false,false],[false,false,true,false,false],[false,true,false,true,true],[false,false,true,false,false],[false,false,true,false,false]],
#  [[false,false,false,false,true],[false,false,true,false,true],[false,true,false,true,true],[false,false,true,false,false],[true,true,true,false,false]]]
# matrix has 6 cities
# my output ******************
# [[[false,true,false,true,false],[true,false,true,true,true],[false,true,false,false,false],[true,true,false,false,true],[false,true,false,true,false]],
#  [[false,false,false,true,false],[false,false,true,true,true],[false,true,false,false,false],[true,true,false,false,true]],
#  [[false,false,false,true,false],[false,false,false,true,false],[false,false,false,false,false],[true,true,false,false,true],[false,false,false,true,false]],
#  [[false,false,false,true,false],[false,false,true,true,false],[false,true,false,true,true],[true,true,true,false,true],[false,false,true,true,false]],
#  [[false,false,false,false,false],[false,false,true,false,false],[false,true,false,true,true],[false,false,true,false,false],[false,false,true,false,false]],
#  [[false,false,false,false,true],[false,true,false,true,true],[false,false,true,false,false],[true,true,true,false,false]]]
# Expected Output:
# [[[false,true,false,true,false],[true,false,true,true,true],[false,true,false,false,false],[true,true,false,false,true],[false,true,false,true,false]],
#  [[false,false,false,true,false],[false,false,true,true,true],[false,true,false,false,false],[true,true,false,false,true],[false,true,false,true,false]],
#  [[false,false,false,true,false],[false,false,false,true,false],[false,false,false,false,false],[true,true,false,false,true],[false,false,false,true,false]],
#  [[false,false,false,true,false],[false,false,true,true,false],[false,true,false,true,true],[true,true,true,false,true],[false,false,true,true,false]]]


"""
{
  "input": {
    "roadRegister": [
      [
        false,
        false,
        false,
        false,
        true,
        false
      ],
      [
        false,
        false,
        true,
        false,
        true,
        false
      ],
      [
        false,
        true,
        false,
        true,
        true,
        true
      ],
      [
        false,
        false,
        true,
        false,
        false,
        false
      ],
      [
        true,
        true,
        true,
        false,
        false,
        true
      ],
      [
        false,
        false,
        true,
        false,
        true,
        false
      ]
    ]
  },
  "output": [
    [
      [
        false,
        true,
        false,
        true,
        false
      ],
      [
        true,
        false,
        true,
        true,
        true
      ],
      [
        false,
        true,
        false,
        false,
        false
      ],
      [
        true,
        true,
        false,
        false,
        true
      ],
      [
        false,
        true,
        false,
        true,
        false
      ]
    ],
    [
      [
        false,
        false,
        false,
        true,
        false
      ],
      [
        false,
        false,
        true,
        true,
        true
      ],
      [
        false,
        true,
        false,
        false,
        false
      ],
      [
        true,
        true,
        false,
        false,
        true
      ],
      [
        false,
        true,
        false,
        true,
        false
      ]
    ],
    [
      [
        false,
        false,
        false,
        true,
        false
      ],
      [
        false,
        false,
        false,
        true,
        false
      ],
      [
        false,
        false,
        false,
        false,
        false
      ],
      [
        true,
        true,
        false,
        false,
        true
      ],
      [
        false,
        false,
        false,
        true,
        false
      ]
    ],
    [
      [
        false,
        false,
        false,
        true,
        false
      ],
      [
        false,
        false,
        true,
        true,
        false
      ],
      [
        false,
        true,
        false,
        true,
        true
      ],
      [
        true,
        true,
        true,
        false,
        true
      ],
      [
        false,
        false,
        true,
        true,
        false
      ]
    ],
    [
      [
        false,
        false,
        false,
        false,
        false
      ],
      [
        false,
        false,
        true,
        false,
        false
      ],
      [
        false,
        true,
        false,
        true,
        true
      ],
      [
        false,
        false,
        true,
        false,
        false
      ],
      [
        false,
        false,
        true,
        false,
        false
      ]
    ],
    [
      [
        false,
        false,
        false,
        false,
        true
      ],
      [
        false,
        false,
        true,
        false,
        true
      ],
      [
        false,
        true,
        false,
        true,
        true
      ],
      [
        false,
        false,
        true,
        false,
        false
      ],
      [
        true,
        true,
        true,
        false,
        false
      ]
    ]
  ]
}
"""



