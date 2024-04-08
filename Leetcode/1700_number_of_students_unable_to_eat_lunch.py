def countStudents(students, sandwiches) -> int:
        st_count = {
            0: 0,
            1: 0
        } 
  

        for student in students:
            if student == 0:
                st_count[0] += 1
            else:
                st_count[1] += 1

        remaining = len(students)

        for sandwich in sandwiches:
            if st_count[sandwich] == 0:
                break
            if remaining == 0:
                break
            
            st_count[sandwich] -= 1
            remaining -= 1

        return remaining


assert countStudents([1,1,0,0], [0,1,0,1]) == 0
assert countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]) == 3
