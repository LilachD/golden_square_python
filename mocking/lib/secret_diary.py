class SecretDiary:
    def __init__(self, diary):
        self._diary = diary
        self._is_locked = True

    def read(self):
        if self._is_locked == True:
            return "Go away!"
        return self._diary.read()

    def lock(self):
        self._is_locked = True

    def unlock(self):
        self._is_locked = False