import asyncio

async def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        print(f'Asyncio.Task: Compute factorial({i})')
        await asyncio.sleep(1)
        fact *= i
    print(f'Asyncio.Task: factorial({number}) = {fact}')

async def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print(f'Asyncio.Task: Compute fibonacci({i})')
        await asyncio.sleep(1)
        a, b = b, a + b
    print(f'Asyncio.Task: fibonacci({number}) = {a}')

async def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / iclera
        print(f'Asyncio.Task: Compute binomial_coefficient({i})')
        await asyncio.sleep(1)
    print(f'Asyncio.Task: binomial_coefficient({n}, {k}) = {result}')

async def main():
    # Create tasks
    task_list = [
        asyncio.create_task(factorial(10)),
        asyncio.create_task(fibonacci(10)),
        asyncio.create_task(binomial_coefficient(20, 10))
    ]
    # Wait for all tasks to complete
    await asyncio.gather(*task_list)

if __name__ == '__main__':
    # Run the main function
    asyncio.run(main())
