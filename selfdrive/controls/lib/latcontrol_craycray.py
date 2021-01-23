from cereal import log


class LatControlCrayCray():
  def __init__(self, CP):
    self.angle_steers_des = 0.

  def reset(self):
    pass

  def update(self, active, CS, CP, path_plan, craycray_sa, roll, curv_factor, sr):
    pid_log = log.ControlsState.LateralPIDState.new_message()
    pid_log.steerAngle = float(craycray_sa)
    pid_log.steerRate = float(CS.steeringRate)

    if CS.vEgo < 0.3 or not active:
      output_steer = 0.0
      pid_log.active = False
    else:
      self.angle_steers_des = path_plan.angleSteers - path_plan.angleOffset  # get from MPC/PathPlanner
      output_steer = (self.angle_steers_des *curv_factor / sr + 0.456*roll) / 0.09207
      pid_log.active = True
      pid_log.output = output_steer
    return output_steer, float(self.angle_steers_des), pid_log
