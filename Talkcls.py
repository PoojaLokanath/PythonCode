class Talk:
    """A class for the talks"""
    def __int__(self, speaker, title, tags):
        self.speaker = speaker
        self.title = title
        self.tags = tags
        
    def get_speaker_firstname(self):
        return self.speaker.split()[0]
        
    def get_tags(self):
        return self.tags.split(',')
    
    
    
    