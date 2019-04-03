Since there is at most one C instruction in this test set, we can solve the two cases independently.

If there is no C instruction in P, then none of our swaps will have any effect, so all we can do is check whether the damage of the beam exceeds D.

If there is one C instruction in P, then we can try every possible position for the C instruction in the program. Assuming that there is at least one position for the C instruction that causes the total damage not to exceed D, we can choose the scenario that requires the fewest swaps; the number of required swaps for a scenario is equal to the distance between the original and final positions of the C instruction.
