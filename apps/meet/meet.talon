app: meet
-

toggle (mute|microphone):
    user.toggle_microphone()

toggle (video|camera):
    user.toggle_camera()

toggle chat:
    user.toggle_chat()

focus chat:
    user.toggle_chat()
    sleep(500ms)
    user.toggle_chat()

toggle people:
    user.toggle_people()

toggle captions:
    user.toggle_captions()

toggle hand:
    user.toggle_hand()

(leave meeting|go back):
    user.leave_meeting()

new meeting:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("2022-03-29_13.46.17.096597.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()

share screen:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("2022-03-29_13.43.50.270361.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()

stop sharing:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("2022-03-29_13.48.48.170315.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()

add others:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("2022-03-29_13.49.27.513916.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()

copy [meeting] details:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("2022-03-29_13.50.00.829771.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()
