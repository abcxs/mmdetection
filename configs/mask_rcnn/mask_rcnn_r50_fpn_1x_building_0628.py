_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/building_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)
