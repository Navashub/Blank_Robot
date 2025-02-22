from repository.RobotRepository import ( get_all_robot_data, get_robot_data_by_id, create_robot_data)

def get_all_robot_service():
    return get_all_robot_data()

def get_robot_data_by_id_service():
    return get_robot_data_by_id()

def create_robot_data_service(video_url, audio_url, motion):
    return create_robot_data(video_url, audio_url, motion)