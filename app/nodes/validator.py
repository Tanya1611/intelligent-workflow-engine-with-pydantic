'''
The validator checks whether the execution result makes sense.
'''

from app.models.execution import ExecutionResult

class ValidatorNode:
    ''' 
    Validates execution results before the workflow proceeds.

    It checks whether execution succeeded, the execution time is valid, and a usable output is available.
    '''

    def process(self, result: ExecutionResult) -> bool:

        if not result.success:
            return False

        if result.execution_time < 0:
            return False

        if result.output is None or result.output.strip() == "":
            return False

        return True
