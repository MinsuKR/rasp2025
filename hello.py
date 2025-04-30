 # GPIO 라이브러리 임포트
import RPi.GPIO as GPIO
# time 라이브러리 임포트
import time

 # 핀번호 할당법은 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# 사용할 핀번호 대입
LED =11

 # 11번 핀을 출력 핀으로 설정, 초기출력은 로우
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

 # 예외 처리
try:
 # 무한반복
	while 1:
 # 하이레벨 출력
		Switch = input()
		if (Switch =='1'):
 			GPIO.output(LED, GPIO.HIGH)
			
 # 0.5초 대기
 			time.sleep(1)
 # 로우레벨 출력
		else:
 			GPIO.output(LED, GPIO.LOW)
			
 # 0.5초 대기
 			time.sleep(1)

 # 키보드 예외를 검출
except Keyboardlnterrupt:
	pass

finally:
	GPIO.cleanup()

