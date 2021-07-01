"""A video player class."""
import random 
import re
random.seed()
from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playingVideoId= '' 
        self.pauseFlag= False 
        self.playFlag = False
        self.playlists = dict()
    def isPlaying(self,video_id):
        if  self.playingVideoId == video_id:
            
            return True
        else:
            
            return False
            

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videoList = self._video_library.get_all_videos()
        print("Here's a list of all videos:")
        for i in  videoList:
          print(f"{i.title},{i.video_id},{i.tags}")
#         

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        
            
        currVideo = self._video_library.get_video(video_id) 
        
        if currVideo is None:
            print('Video not found')
            return 
        if self.isPlaying(currVideo.video_id):
            
            self.stop_video(video_id)
            self.playFlag= False
            self.playingVideoId = ''
            
        else:
            self.playFlag = True
            if self.pauseFlag: self.pauseFlag = False
            print(f"Playing video: {currVideo.title}")
            self.playingVideoId = currVideo.video_id
        
        
          
    def stop_video(self,video_id):
        """Stops the current video."""
        if self.playingVideoId != '':
            if video_id==None:
                print(f'Stopping video: {self._video_library.get_video(self.playingVideoId).title}')
                self.playFlag = False
                
                self.playingVideoId=''
            
            else:
                print(f'Stopping video: {self._video_library.get_video(video_id).video_id}')
               
                self.playingVideoId =''
        else:
            print('no video playing')
       
           

    def play_random_video(self):
        """Plays a random video from the video library."""
        
        if self.isPlaying(self.playingVideoId):
            self.stop_video(self.playingVideoId)

            totalVideos = self._video_library.get_videos_length()
            randomIndex = random.randint(0,totalVideos-1)
           
            self.play_video(self._video_library.get_all_videos()[randomIndex].video_id)
            
            
        else:
            self.stop_video(self.playingVideoId)
            
            
    def pause_video(self):
        """Pauses the current video."""
        if self.playFlag:
            
            if self.pauseFlag:
                print('video already paused')
            else:
                print(
                    f'Pausing video: {self._video_library.get_video_title(self.playingVideoId)}')
                self.pauseFlag = True
        else:
                self.pauseFlag = False
                print('cannot pause')
        


    def continue_video(self):
        """Resumes playing the current video."""
        if not self.playFlag:
            print('no video playing')
        else:  
            if self.pauseFlag:
                print('continuing video')
                self.pauseFlag = False
            else:
                
                print('Cannot continue')
                

    def show_playing(self):
        """Displays video currently playing."""
        if self.playFlag:
            if not self.pauseFlag:
                print(f"CURRENTLY PLAYING:{self.playingVideoId}")
            else:
                print(f"CURRENTLY PLAYING:{self.playingVideoId} - PAUSED")
            
        else:
            print('no video playing')

    def isInPlaylists(self,playlist_name): 
        
        if len(self.playlists.keys()) > 0:
            for playlist in self.playlists.keys():
                if playlist == playlist_name:
                    return True
                else:
                    return False
        else:
            return False  
            
    def isInPlaylist(self,video,playlist_name): #takes in video object
        
        try:
            if len(video.video_id)>0:
                if self.isInPlaylists(playlist_name):
                    #checks whether video is in playlist 
                    if len(self.playlists[playlist_name])>0:
                        for savedVideo in self.playlists[playlist_name]:
                            if video.video_id == savedVideo.video_id:
                                print('1st')
                                return True
                            
                            else:
                                print('2nd')
                                return False
                                
                    else:
                        print('3rd')
                        return False
                
                else:
                    print('4th')
                    return False
            else:
                return None
        except AttributeError:
            return None
        
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if not self.isInPlaylists(playlist_name):
            self.playlists[playlist_name] = list()
        else:
            print(
                'Cannot create playlist: A playlist with the same name already exists')
        
    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        try:
            if not self.isInPlaylist(self._video_library.get_video(video_id),playlist_name):
                
                self.playlists[playlist_name].append((self._video_library.get_video(video_id)))
                print(f'Added video to {playlist_name}: {video_id}')
            else:
                print(f'Cannot add video to {playlist_name}:Video already added')
                #if not print message
        except AttributeError: 
        
        #else:#self.isInPlaylist(video_id, playlist_name) == None:
            print(f'Cannot add video to {playlist_name}: Video does not exist')
        except KeyError:
            print(f'Playlist does not exist: {playlist_name}')
    def show_all_playlists(self):
        """Display all playlists."""
        
        if len(self.playlists.keys()) >0:
            print('Showing all playlists:')
            for playlist in self.playlists.keys():
                
                print(f'{playlist}')
        else:
            print('No playlists exist yet')

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if self.isInPlaylists(playlist_name):
           
            print(f'Showing playlist: {playlist_name}')
            if len(self.playlists[playlist_name])>0:
                
                for video in self.playlists[playlist_name]:
                    
                    print(f'{video.title,video.video_id, video.tags}')
                    
            else:
                    print('No videos here yet')
        else:
            print(f'Cannot show: {playlist_name}: Playlist does not exist')

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        try:
            if self.isInPlaylists(playlist_name):
                if self.isInPlaylist(self._video_library.get_video(video_id),playlist_name):
                    video = self._video_library.get_video(video_id)
                    self.playlists[playlist_name].remove(video)
                    print(f'Removed video from {playlist_name},": " {video.title}')
                else:
                    print(f'Cannot remove video from {playlist_name}: Video does not exist')
            else:
                print(f'Cannot remove video from playlist: {playlist_name}: Playlist does not exist')
                      
        except KeyError:
            print('Cannot remove video')
 
    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if self.isInPlaylists(playlist_name):
            self.playlists[playlist_name].clear()
            print(f'Successfully removed all videos from {playlist_name}')
        else:
            print(f'Cannot clear playlist {playlist_name}: Playlist does not exist')
            
    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if self.isInPlaylists(playlist_name):
            self.playlists.pop(playlist_name)
            print(f'Deleted playlist {playlist_name}')
        else:
            print(f'Cannot delete playlist {playlist_name}: Playlist does not exist')
 
    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        vidList = self._video_library.get_all_videos()
        results = []
        
        
        for vid in vidList:
            if search_term.upper() in vid.title.upper():         
                results.append(vid)
        
        
        if len(results)>0:
            print(f'Here are the results for {search_term}')
            index = 0
            for vid in results:
                index+=1
                print(f'{index}) {vid.title}')
            print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
            videoNumber=int(input())-1
            try:
                self.play_video(results[videoNumber].video_id)
            except KeyError:
                print('No such video.')
        else:
            print(f'No search results for {search_term}')
            
    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        vidList = self._video_library.get_all_videos()
        results = []
        if '#' in video_tag:
            for vid in vidList:
                for tag in vid.tags: 
                    if video_tag.upper() in tag.upper():
                        results.append(vid)

            if len(results) > 0:
                print(f'Here are the results for {video_tag}')
                index = 0
                for vid in results:
                    index += 1
                    print(f'{index}) {vid.title}, [{vid.tags}]')
                print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
                videoNumber = int(input())-1
                try:
                    self.play_video(results[videoNumber].video_id)
                except KeyError:
                    print('No such video.')
            else:
                print(f'No search results for {video_tag}')
        else:
            print(f'No search results for {video_tag}')
    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
