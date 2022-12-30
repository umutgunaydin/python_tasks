# Write a function named fix_sorted that takes a list with some parts in reverse order
# and fixes it by reversing reverse-sorted parts using a stack.
# There will be no duplicate elements
import stack


def fix_sorted(lis):
    fixed_list = []
    fixer_stack = stack.create_stack()

    for i in range(len(lis) - 1):

        if lis[i] > lis[i + 1]:
            stack.push_stack(lis[i], fixer_stack)
        else:
            fixed_list.append(lis[i])

        if i + 1 == len(lis) - 1:
            fixed_list.append(lis[i + 1])
            while not stack.is_empty_stack(fixer_stack):
                fixed_list.append(stack.pop_stack(fixer_stack))

        while (not stack.is_empty_stack(fixer_stack)) and stack.top_stack(fixer_stack) < lis[i + 1]:
            fixed_list.append(stack.pop_stack(fixer_stack))

    print(fixed_list)


fix_sorted([1, 2, 6, 5, 4, 3, 10, 15, 18, 17])
