from _Framework.MixerComponent import MixerComponent
from _Framework.ButtonElement import ButtonElement
from .SpecialChannelStripComponent import SpecialChannelStripComponent
class SpecialMixerComponent(MixerComponent):
    ' Special mixer class that uses return tracks alongside midi and audio tracks '
    __module__ = __name__

    def __init__(self, num_tracks):
        MixerComponent.__init__(self, num_tracks)
        self._toggle_arm_button = None
        self._toggle_arm_exclusive_button = None

    def tracks_to_use(self):
        return tuple(self.song().visible_tracks) + tuple(self.song().return_tracks)

    def _create_strip(self):
        return SpecialChannelStripComponent()

    def set_toggle_arm_in_selected_track_button(self, button):
        assert isinstance(button, (ButtonElement, type(None)))
        if (button != self._toggle_arm_button):
            if (self._toggle_arm_button != None):
                self._toggle_arm_button.remove_value_listener(self.toggle_arm)
            self._toggle_arm_button = button
            if (self._toggle_arm_button != None):
                self._toggle_arm_button.add_value_listener(self.toggle_arm)
            self.update()

    def set_toggle_arm_exclusive_in_selected_track_button(self, button):
        assert isinstance(button, (ButtonElement, type(None)))
        if (button != self._toggle_arm_exclusive_button):
            if (self._toggle_arm_exclusive_button != None):
                self._toggle_arm_exclusive_button.remove_value_listener(self.toggle_arm_exclusive)
            self._toggle_arm_exclusive_button = button
            if (self._toggle_arm_exclusive_button != None):
                self._toggle_arm_exclusive_button.add_value_listener(self.toggle_arm_exclusive)
            self.update()

    def toggle_arm_track(self, track, exclusive):
        if track.can_be_armed:
            track.arm = not track.arm
        if exclusive: # arm exclusive
            song = self.song()
            for t in song.tracks:
                if not t == track and t.can_be_armed:
                    t.arm = False

    def toggle_arm(self, value):
        if ((value != 0) or (not self._toggle_arm_button.is_momentary())):
            self.toggle_arm_track(self.song().view.selected_track, self.song().exclusive_arm)

    def toggle_arm_exclusive(self, value):
        if ((value != 0) or (not self._toggle_arm_exclusive_button.is_momentary())):
            self.toggle_arm_track(self.song().view.selected_track, True)

