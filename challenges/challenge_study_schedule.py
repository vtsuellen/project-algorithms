def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    students_count = 0 

    try: 
        for student in permanence_period:
            if student[0] <= target_time <= student[1]:
                students_count += 1
        return students_count
    
    except TypeError:
        return None
