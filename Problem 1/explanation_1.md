Explanation:
CTE (Common Table Expression) RankedSalaries:
- We use the DENSE_RANK() window function to assign a rank to each salary within a department. This ensures that the top three unique salaries get ranks 1, 2, and 3.

The PARTITION BY e.departmentId ensures that the ranking is done separately for each department.

The ORDER BY e.salary DESC sorts the salaries in descending order, so that the highest salary gets rank 1.

Main Query:
- We join the RankedSalaries CTE with the Department table to get the department names.
- We filter out the employees who have a salary rank of 3 or lower (WHERE rs.salary_rank <= 3).
- The result is sorted by the department name and salary in descending order to match the expected output format.
