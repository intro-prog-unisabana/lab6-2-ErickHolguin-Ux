def trigger_alarm(temperatures, threshold=80):
  
    triggered = []
    for sensor, temp in temperatures.items():
        if temp > threshold:
            triggered.append(sensor)
    return triggered




   
   
