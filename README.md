# Icinga / Nagios checks for nvidia jetson devices

## Requirements

```pip install jetson-stats```

## gpu temp

```check_jetson_gpu_temp.py -w <warning-level> -c <critical-level```

## gpu ram

```check_jetson_gpu_ram.py -w <warning-level> -c <critical-level```

## gpu tboard

```check_jetson_tboard_temp.py -w <warning-level> -c <critical-level```

## thermal temp

```check_jetson_thermal_temp.py -w <warning-level> -c <critical-level```