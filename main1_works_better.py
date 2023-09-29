import pygame
import random
import time

# global variables
width = 1200
height = 600
n = 1200
wanna_sort = False


# function to draw a single bar on screen

def make_bar(x, y, bar_width, bar_height):
    bar = pygame.Rect(x, y, bar_width, bar_height)
    pygame.draw.rect(screen, pygame.Color("orange"), bar)


# function that divide a screen to 'n' elements and loop the draing function to draw all bars at the screeen
def visualize_bar(x):
    for k in range(len(array)):
        make_bar(x, height - array[k], width / n, array[k])
        x = x + width / n


def bubble_sort():
    tic = time.perf_counter()
    for i in range(len(array) - 1):
        # cleaning the screen after last animation
        screen.fill((67, 67, 67))
        # assagning the origin coordinates
        # using a function to visualize all the bars on the screen
        visualize_bar(x)
        for k in range(len(array) - 1):
            first_element = array[k]
            secound_element = array[k + 1]
            if first_element < secound_element:
                array[k + 1] = first_element
                array[k] = secound_element
        # update screen
        pygame.display.flip()
    toc = time.perf_counter()
    print("sorting took", (toc - tic))


def insertion_sort():
    tic = time.perf_counter()
    for i in range(0, len(array)):
        screen.fill((67, 67, 67))
        visualize_bar(x)
        value = array[i]
        j = i - 1
        while j >= 0 and value < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            array[j + 1] = value

        # update screen
        pygame.display.flip()
    toc = time.perf_counter()
    print("sorting took", (toc - tic))
    print(array)


def merge_sort():
    tic = time.perf_counter()

    def merge(left, right):
        # If the first array is empty, then nothing needs
        # to be merged, and you can return the second array as the result
        if len(left) == 0:
            return right

        # If the second array is empty, then nothing needs
        # to be merged, and you can return the first array as the result
        if len(right) == 0:
            return left

        result = []
        index_left = index_right = 0

        # Now go through both arrays until all the elements
        # make it into the resultant array
        while len(result) < len(left) + len(right):
            # The elements need to be sorted to add them to the
            # resultant array, so you need to decide whether to get
            # the next element from the first or the second array
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

            # If you reach the end of either array, then you can
            # add the remaining elements from the other array to
            # the result and break the loop
            if index_right == len(right):
                result += left[index_left:]
                break

            if index_left == len(left):
                result += right[index_right:]
                break

        return result

    def merge_sort(array):
        # If the input array contains fewer than two elements,
        # then return it as the result of the function
        if len(array) < 2:
            return array

        midpoint = len(array) // 2

        # Sort the array by recursively splitting the input
        # into two equal halves, sorting each half and merging them
        # together into the final result
        return merge(
            left=merge_sort(array[:midpoint]),
            right=merge_sort(array[midpoint:]))

    toc = time.perf_counter()
    print('the time ',toc - tic)


def selectionSort():
    tic = time.perf_counter()
    for s in range(len(array)):
        screen.fill((67, 67, 67))
        visualize_bar(x)
        min_idx = s

        for i in range(s + 1, len(array)):

            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])
        pygame.display.flip()
    toc = time.perf_counter()
    print('time is equal ',toc-tic)



def shuffle():
    array = []
    for h in range(n):
        array.append(random.randrange(1, height / 2))
    return array


def clean_the_screen():
    screen.fill((67, 67, 67))
    visualize_bar(x)
    pygame.display.flip()


# function to visualize bar chart

# initialize pygame screen
pygame.init()
screen = pygame.display.set_mode((width, height))

# animation loop
array = shuffle()

x = 0
y = 200
screen.fill((67, 67, 67))
visualize_bar(x)

pygame.display.flip()
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                bubble_sort()
            if event.key == pygame.K_2:
                insertion_sort()
            if event.key == pygame.K_3:
                selectionSort()
            if event.key == pygame.K_4:
                merge_sort()
            if event.key == pygame.K_s:
                array = shuffle()
                clean_the_screen()
