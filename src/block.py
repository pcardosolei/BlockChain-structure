class Block:
    def __init__(prevHash,transationData,timestamp):
        self.prevHash = prevHash
        self.transationData = transationData
        self.timestamp = timestamp

    def getHashBlock():
        return hash(self)