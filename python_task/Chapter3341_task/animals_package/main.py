import birds_package.Eagle as eagles
import mammals_package.Dog as dogs


def eagle() :
    eagle = eagles.Eagle.family()
    return eagle

dog = dogs.Dog()
print(dog.family())


