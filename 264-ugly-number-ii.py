class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initialize an array to store the first n ugly numbers
        ugly_numbers = [1]

        # Initialize pointers to the next numbers to multiply by the factors 2, 3, and 5
        i2, i3, i5 = 0, 0, 0

        # Iterate until the array of ugly numbers has n elements
        while len(ugly_numbers) < n:
            # Calculate the next potential ugly number by multiplying the current numbers
            # pointed to by the i2, i3, and i5 pointers by 2, 3, and 5, respectively
            next_ugly_number = min(
                ugly_numbers[i2]*2, ugly_numbers[i3]*3, ugly_numbers[i5]*5)

            # If the next potential ugly number is not already in the array, add it to the array
            if next_ugly_number not in ugly_numbers:
                ugly_numbers.append(next_ugly_number)

            # Increment the pointers to the next numbers to multiply by the factors 2, 3, and 5, as needed
            if next_ugly_number == ugly_numbers[i2]*2:
                i2 += 1
            if next_ugly_number == ugly_numbers[i3]*3:
                i3 += 1
            if next_ugly_number == ugly_numbers[i5]*5:
                i5 += 1

        # Return the nth ugly number
        return ugly_numbers[-1]
