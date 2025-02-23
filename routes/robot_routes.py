from flask import Blueprint, jsonify, request
from services.robot_service import (get_all_robot_service, get_robot_data_by_id_service, create_robot_data_service)

robot_bp = Blueprint('robot', __name__)

@robot_bp.route('/api/v1/robot_data', methods=['GET'])
def get_robot_data():
    
    robot_data = get_all_robot_service()
    data_list = [{
        'id' : data.id,
        'video_url' : data.video_url,
        'audio_url' : data.audio_url,
        'motion' : data.motion,
        'timestamp' : data.timestamp
    } for data in robot_data]
    return jsonify({'robot_data' : data_list})

@robot_bp.route('/api/v1/robot_data', methods=['POST'])
def create_robot_data_route():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'invalid JSONdata'}), 400
    
    video_url = data.get("video_url")
    audio_url = data.get("audio_url")
    motion = data.get("motion", "STOP")
    
    if not video_url or not audio_url or not motion:
        return jsonify({'error' : 'Missing required fields'}), 400 
    
    new_robot_id = create_robot_data_service(video_url, audio_url, motion)
    
    return jsonify({'message' : 'Robot data stored successfully', 'robot_id' : new_robot_id}), 201


@robot_bp.route('/api/v1/robot_data/<int:data_id>', methods=['GET'])
def get_robot_data_by_id_route(data_id):
    data = get_robot_data_by_id_service(data_id)
    if data:
        return jsonify({
            'id' : data.id,
            'video_url' : data.video_url,
            'audio_url' : data.audio_url,
            'motion' : data.motion,
            'timestamp' : data.timestamp
        }), 200
    else:
        return jsonify({'error' : 'Robot data not found'}), 404