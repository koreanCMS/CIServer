# -*- coding: utf-8 -*-
import sys
import io
import unittest
import os
import setUp
import time
import random
from Autoscroll import *
from Exception import *
from opencv import *
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from random import randint
import numpy as np
# change test of page master page master page master
ini = 0
driver = 'driver'
final_check = 0
pass_check = 0

class TCFG():
	res=[]
	elList=[]
	cheerCNT=0

class And(unittest.TestCase):
	def setUp(self):
		global ini, driver, res, elList
		if ini == 0:
			setUp.setUp(self)
			driver = self.driver
			ini += 1
			self.reso = self.driver.get_window_size()
			TCFG.res.append(self.reso["width"])
			TCFG.res.append(self.reso["height"])
			TCFG.elList=[]
			TCFG.cheerCNT=0

	def test_40_My_Aritaum(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 마이아리따움
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
				sleep(2)
				# 나의리뷰까지
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0040 Passed (Watch List of My Aritaum)")
				pass_check = 1
				break

	def test_41_Mileage(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 아리따움 마일리지
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="아리따움 마일리지"]'))).click()
				sleep(2)
				# 사용/적립내역 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="사용/적립내역"]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0041 Passed (Watch Page of Mileage)")
				pass_check = 1
				break

	def test_42_BP(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 뷰티포인트
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="뷰티포인트"]'))).click()
				sleep(2)
				# 사용/적립내역 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="사용/적립내역"]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0042 Passed (Watch Page of Beauty Point)")
				pass_check = 1
				break

	def test_43_Beautycon(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 뷰티콘
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="뷰티콘"]'))).click()
				sleep(2)
				# 뷰티콘 조회 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="뷰티콘 조회"]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0043 Passed (Watch Page of Beautycon)")
				pass_check = 1
				break

	def test_44_Coupon(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 쿠폰
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="쿠폰"]'))).click()
				sleep(2)
				# 쿠폰등록 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="쿠폰등록"]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0044 Passed (Watch Page of Coupon)")
				pass_check = 1
				break

	def test_45_Delivery(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 주문배송조회
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="주문배송조회"]'))).click()
				sleep(2)
				# 주문/배송 조회 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="주문/배송 조회"]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0045 Passed (Watch Page of Delivery)")
				pass_check = 1
				break


	def test_46_Delivery_Setting(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 정기배송 설정
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/text_delivery_setting'))).click()
				sleep(2)
				# 정기배송관리 타이틀 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="정기배송관리"]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0046 Passed (Watch Page of Delivery Setting)")
				pass_check = 1
				break

	def test_47_My_Review(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 나의 리뷰
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/l_lay_my_review'))).click()
				sleep(2)
				# 작성가능한 리뷰 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[contains(@text,"작성가능한 리뷰")]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0047 Passed (Watch Page of My Review)")
				pass_check = 1
				break

	def test_48_Beauty_Service(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 로그아웃까지 내리기 (하단 바 내리기)
				scroll_find(self,driver,'com.aritaum1:id/l_lay_log_out')
				# 뷰티서비스
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/l_lay_beauty_service'))).click()
				sleep(2)
				# 전체 스피너 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Spinner[@text="전체"]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0048 Passed (Watch Page of Beauty Service)")
				pass_check = 1
				break

	def test_49_Winning_Check(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 당첨확인
				scroll_click(self,driver,'com.aritaum1:id/l_lay_win_check')
				# 전체 스피너 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Spinner[@text="전체"]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0049 Passed (Watch Page of Winning Check)")
				pass_check = 1
				break

	def test_50_Shopping_Card(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 쇼핑카드
				scroll_click(self,driver,'com.aritaum1:id/l_lay_shopping_card')
				# 보유 쇼핑카드 텍스트 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[contains(@text,"보유 쇼핑카드")]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0050 Passed (Watch Page of Shopping Card)")
				pass_check = 1
				break

	def test_51_Giftcard(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 기프트카드
				scroll_click(self,driver,'com.aritaum1:id/l_lay_gift_card')
				# 보유카드 텍스트 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[contains(@text,"보유카드")]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0051 Passed (Watch Page of Giftcard)")
				pass_check = 1
				break


	def test_52_Edit_Info(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 회원정보수정
				scroll_click(self,driver,'com.aritaum1:id/l_lay_edit_user_info')
				try:
					# 로그인정보가 없습니다.
					wait.until(EC.presence_of_element_located((By.ID, 'com.sec.android.app.sbrowser:id/js_modal_dialog_message')))
					# 확인
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="확인"]'))).click()
					sleep(2)
				except:
					pass
				# 뷰티포인트 화면전체
				wait.until(EC.presence_of_element_located((By.ID, 'com.sec.android.app.sbrowser:id/content_layout')))
				# 뒤로
				driver.back()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0052 Passed (Watch Page of Edit Info)")
				pass_check = 1
				break

	def test_53_Shipping_Management(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 배송지 관리
				scroll_click(self,driver,'com.aritaum1:id/l_lay_shipping_manager')
				# 신규 배송지
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="신규 배송지"]')))
				# 뒤로 (<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움 텍스트
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))
				# 뒤로 (<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 배너이미지
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/banner_image_view')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
					sleep(2)
					# 나의리뷰까지
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/l_lay_my_review')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0051 Passed (Watch Page of Giftcard)")
				pass_check = 1
				break

	def test_54_CreditCard_Purchase(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 세일
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="세일"]'))).click()
				sleep(2)
				# 첫번째 상품
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/img_thumb'))).click()
				sleep(2)
				# 상품이미지
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/frescoImageView')))
				# 구매하기
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/rl_button_buy_layout'))).click()
				sleep(2)
				# 상품 옵션있는경우
				try:
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/rl_option_layout'))).click()
					sleep(2)
					ep = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[contains(@text,"옵션을 선택")]')))
					TouchAction(driver).tap(None, ep.location['x']+100, ep.location['y']+165, 1).perform()
					sleep(3)
				except:
					pass
				# 바로구매
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/rl_buy_buy_layout'))).click()
				sleep(2)
				# 주문/결제 페이지까지
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="주문/결제"]')))
				# 뒤로
				driver.back()
				sleep(2)
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/rl_buy_buy_layout')))
				driver.back()
				sleep(2)
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/rl_button_buy_layout')))
				driver.back()
				sleep(2)
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/banner_image_view')))
				# 홈
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="홈"]'))).click()
				sleep(2)
				# 베스트셀러
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/text_main_title')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ARM_0054 Passed (Check List of Payment)")
				pass_check = 1
				break

	def test_57_Product_Detail(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 베스트셀러의 더보기
				scroll_find(self,driver,'com.aritaum1:id/text_more')
				# 임의상품 클릭
				wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.ImageView[@resource-id="com.aritaum1:id/img_thumb"])[%s]'%np.random.randint(1,4)))).click()
				sleep(2)
				# 상품 이미지 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/frescoImageView')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0057 Passed (Watch List of Product Detail)")
				pass_check = 1
				break

	def test_58_Product_Brand(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 브랜드관 클릭
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/tv_brand_name_text'))).click()
				sleep(2)
				# 전체상품 텍스트
				scroll_find_xpath(self,driver,'//android.widget.Button[@text="전체상품"]')
				# 뒤로
				driver.back()
				sleep(2)
				# 상품 이미지 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/frescoImageView')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 베스트셀러의 더보기
					scroll_find(self,driver,'com.aritaum1:id/text_more')
					# 임의상품 클릭
					wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.ImageView[@resource-id="com.aritaum1:id/img_thumb"])[%s]'%np.random.randint(1,4)))).click()
					sleep(2)
					# 상품 이미지 노출
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/frescoImageView')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0058 Passed (Watch List of Brand Page)")
				pass_check = 1
				break

	def test_59_Product_Live_Feed(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 베스트 리뷰 까지 내리기
				scroll_find_xpath(self,driver,'//android.widget.TextView[@text="베스트 리뷰"]')
				# Live Feed 페이지 이동
				ep = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="# Live Feed"]')))
				TouchAction(driver).tap(None, ep.location['x']+150, ep.location['y']+300, 1).perform()
				sleep(3)
				# 구매하기 버튼 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/txt_prd_buy')))
				# 닫기(X)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/img_close'))).click()
				sleep(2)
				# 구매하기 버튼 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/rl_button_buy_layout')))
				# 뒤로
				driver.back()
				sleep(2)
				# 베스트셀러 텍스트까지
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/text_main_title')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 베스트셀러의 더보기
					scroll_find(self,driver,'com.aritaum1:id/text_more')
					# 임의상품 클릭
					wait.until(EC.element_to_be_clickable((By.ID, '(//android.widget.ImageView[@resource-id="com.aritaum1:id/img_thumb"])[%s]'%np.random.randint(1,4)))).click()
					sleep(2)
					# 상품 이미지 노출
					wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/frescoImageView')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0059 Passed (Watch List of Live Feed)")
				pass_check = 1
				break

	def test_60_Product_Sale(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 세일
				scroll_xpath_LR(self, driver, '//android.widget.TextView[@text="베스트"]', '//android.widget.TextView[@text="세일"]',loc=TCFG.res[0]*0.9, x1=TCFG.res[0]*0.2, x2=TCFG.res[0]*0.5,direction=16)
				# 첫번째 상품
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/img_thumb'))).click()
				sleep(2)
				# 상품 이미지 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/frescoImageView')))
				# 할인가 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/tv_standard_discount_text')))
				# 뒤로
				driver.back()
				sleep(2)
				# 배너이미지
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/banner_image_view')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0060 Passed (Watch price of discounted)")
				pass_check = 1
				break

	def test_61_Search_Hera(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 홈 클릭
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="홈"]'))).click()
				sleep(2)
				# 베스트셀러 텍스트까지
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/text_main_title')))
				# 검색버튼 클릭
				scroll_click_back(self,driver,'com.aritaum1:id/header_search_image_view')
				# 최근검색어 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="최근검색어"]')))
				# 헤라 검색
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/word_edit_text'))).send_keys('헤라')
				sleep(2)
				# 헤라 브랜드관 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="헤라 브랜드관"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0061 Passed (Watch List of Hera Search)")
				pass_check = 1
				break

	def test_62_Search_Nothing(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# ㄱㄴㄷㄹ 검색
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/word_edit_text'))).send_keys('ㄱㄴㄷㄹ')
				sleep(2)
				# 검색(돋보기 아이콘)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_search_image_view'))).click()
				sleep(2)
				# 아쉽게도 검색어와 일치하는 내용이 없습니다.  텍스트 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[contains(@text,"일치하는 내용이 없습니다")]')))
				# 뒤로 (EditText를 잡을수 없기때문에 뒤로가기함)
				driver.back()
				sleep(2)
				# 돋보기 아이콘
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/header_search_image_view')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 검색버튼 클릭
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_search_image_view'))).click()
					sleep(2)
					# 최근검색어 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="최근검색어"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0062 Passed (Watch List of Meaningless Search)")
				pass_check = 1
				break

	def test_63_Search_IOPE(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 아 검색
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/word_edit_text'))).send_keys('아')
				sleep(2)
				# 아이오페 클릭
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="아이오페"]'))).click()
				sleep(2)
				# 아이오페 브랜드관 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="아이오페 브랜드관"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 검색버튼 클릭
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_search_image_view'))).click()
					sleep(2)
					# 최근검색어 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="최근검색어"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0063 Passed (Watch List of '아' Search)")
				pass_check = 1
				break

	def test_64_My_Review(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 마이아리따움
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]'))).click()
				sleep(2)
				# 나의리뷰
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/l_lay_my_review'))).click()
				sleep(2)
				# 작성가능한 리뷰 버튼 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[contains(@text,"작성가능한 리뷰")]')))
				# 홈
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="홈"]'))).click()
				sleep(2)
				# 배너이미지
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/banner_image_view')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0064 Passed (Watch List of My Review)")
				pass_check = 1
				break

	def test_65_Single_Product(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 검색버튼 클릭
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_search_image_view'))).click()
				sleep(2)
				# 최근검색어 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="최근검색어"]')))
				# 벤츠 클럽 블루 EDT 검색
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/word_edit_text'))).send_keys('벤츠 클럽 블루 EDT')
				sleep(2)
				# 검색(돋보기 아이콘)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_search_image_view'))).click()
				sleep(2)
				# 상품 이미지까지 대기
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/img_thumb')))
				# 상품 클릭
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="벤츠 클럽 블루 EDT"]'))).click()
				sleep(2)
				# 상품이미지 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/frescoImageView')))
				# 구매하기
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/rl_button_buy_layout'))).click()
				sleep(2)
				# 장바구니 담기
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/tv_cart_btn_text'))).click()
				sleep(2)
				# 뒤로
				driver.back()
				sleep(2)
				# 구매하기 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/rl_button_buy_layout')))
				# 장바구니 가기
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_cart_image_view'))).click()
				sleep(2)
				# 장바구니 타이틀
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="장바구니"]')))
				# 담은 상품명 노출
				scroll_find_xpath(self,driver,'//android.view.View[@text="벤츠 클럽 블루 EDT 아리따움"]')
				# 홈 아이콘
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_home_image_view'))).click()
				sleep(2)
				# 배너이미지
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/banner_image_view')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0065 Passed (Watch List of Single Product Added To Cart)")
				pass_check = 1
				break

	def test_66_Option_Product(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 검색버튼 클릭
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_search_image_view'))).click()
				sleep(2)
				# 최근검색어 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="최근검색어"]')))
				# 슈가볼 쿠션 블러셔 검색
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/word_edit_text'))).send_keys('슈가볼 쿠션 블러셔')
				sleep(2)
				# 검색(돋보기 아이콘)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_search_image_view'))).click()
				sleep(2)
				# 상품 이미지까지 대기
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/img_thumb')))
				# 상품 클릭
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="슈가볼 쿠션 블러셔"]'))).click()
				sleep(2)
				# 상품이미지 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/frescoImageView')))
				# 구매하기
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/rl_button_buy_layout'))).click()
				sleep(2)
				# 상품 옵션
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/rl_option_layout'))).click()
				sleep(2)
				# 3호
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[contains(@text,"3호")]'))).click()
				sleep(2)
				# 장바구니 담기
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/tv_cart_btn_text'))).click()
				sleep(2)
				# 뒤로
				driver.back()
				sleep(2)
				# 구매하기 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/rl_button_buy_layout')))
				# 장바구니 가기
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_cart_image_view'))).click()
				sleep(2)
				# 장바구니 타이틀
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="장바구니"]')))
				# 담은 상품명 노출
				scroll_find_xpath(self,driver,'//android.view.View[@text="슈가볼 쿠션 블러셔 아리따움"]')

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0066 Passed (Watch List of Option Product Added To Cart)")
				pass_check = 1
				break


	def test_67_Cart_Number(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 상품수량 과 가격
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@text="1"]')))
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[contains(@text,"69,000")]')))
				# 수량 증가
				wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.Button[@text="+"])[1]'))).click()
				# 상품수량 과 가격
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@text="2"]')))
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[contains(@text,"138,000")]')))

				# 수량 감소
				wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.Button[@text="-"])[1]'))).click()
				# 상품수량 과 가격
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@text="1"]')))
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[contains(@text,"69,000")]')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 장바구니
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_cart_image_view'))).click()
					sleep(2)
					# 장바구니 타이틀
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="장바구니"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0067 Passed (Change Product Quantity)")
				pass_check = 1
				break

	def test_68_Change_Order(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 옵션 셀렉트박스 선택
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[contains(@text,"3호")]'))).click()
				sleep(2)
				# 2호로 변경
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[contains(@text,"2호")]'))).click()
				sleep(2)
				# 변경전 옵션 미노출 확인
				wait.until(EC.invisibility_of_element_located((By.XPATH, '//android.widget.Button[contains(@text,"3호")]')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 장바구니
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_cart_image_view'))).click()
					sleep(2)
					# 장바구니 타이틀
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="장바구니"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0068 Passed (Change Product Option)")
				pass_check = 1
				break

	def test_69_Uncheck_Product(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 전체선택 해제
				wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.CheckBox)[1]'))).click()
				sleep(2)
				# 0개 상품 주문하기
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="0개 상품 주문하기"]')))
				# 첫번째 상품 체크
				wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.CheckBox)[2]'))).click()
				sleep(2)
				# 1개 상품 주문하기
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="1개 상품 주문하기"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 장바구니
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_cart_image_view'))).click()
					sleep(2)
					# 장바구니 타이틀
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="장바구니"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0069 Passed (Check Action of Uncheck Product)")
				pass_check = 1
				break


	def test_70_Delete_Product(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 첫번째 상품 삭제
				wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.Button[@text="장바구니에서 상품 삭제"])[1]'))).click()
				sleep(2)
				# 해당 상품을 장바구니에서 삭제하시겠습니까? 창 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[contains(@text,"삭제하시겠습니까?")]')))
				# 확인
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="확인"]'))).click()
				sleep(2)
				# 삭제한 상품 미노출 확인
				wait.until(EC.invisibility_of_element_located((By.XPATH, '//android.view.View[@text="벤츠 클럽 블루 EDT 아리따움"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 장바구니
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_cart_image_view'))).click()
					sleep(2)
					# 장바구니 타이틀
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="장바구니"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0070 Passed (Check Action of Delete Product)")
				pass_check = 1
				break

	def test_71_Cart_Payment(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 전체상품 선택
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.CheckBox[contains(@text,"전체선택")]'))).click()
				sleep(2)
				# 0개 상품 주문하기 미노출
				wait.until(EC.invisibility_of_element_located((By.XPATH, '//android.view.View[@text="0개 상품 주문하기"]')))
				# 상품 주문하기
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[contains(@text,"상품 주문하기")]'))).click()
				sleep(2)
				# 주문/결제 타이틀 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="주문/결제"]')))
				# 뒤로(<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 홈으로
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_home_image_view'))).click()
				sleep(2)
				# 배너
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/banner_image_view')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 장바구니
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_cart_image_view'))).click()
					sleep(2)
					# 장바구니 타이틀
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="장바구니"]')))
					# 전체상품 해제
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.CheckBox[contains(@text,"전체선택")]'))).click()
					sleep(2)
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0071 Passed (Watch List of Cart)")
				pass_check = 1
				break

	def test_72_Dial(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 마이아리따움
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/toolbar_mypage_text_view'))).click()
				sleep(2)
				# 나의 리뷰 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="나의 리뷰"]')))
				# 고객센터
				scroll_click(self,driver,'com.aritaum1:id/l_lay_customer')
				# 챗봇상담하기 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="챗봇 상담하기"]')))
				# 다이얼
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[contains(@text,"온라인 고객센터 대표전화")]'))).click()
				sleep(2)
				# 연락처에 추가 텍스트 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[contains(@text,"연락처에 추가")]')))
				# 뒤로
				driver.back()
				sleep(2)
				# 최근기록 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.samsung.android.contacts:id/dialpad_tab_text_view')))
				# 뒤로
				driver.back()
				sleep(2)
				# 고객센터 타이틀 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/header_title_text_view')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0072 Passed (Watch Page of Dial)")
				pass_check = 1
				break

	def test_73_Chatbot(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 챗봇 상담하기
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="챗봇 상담하기"]'))).click()
				sleep(2)
				# 전송 텍스트 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="send"]')))
				# 뒤로 (<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 1:1 상담 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="1:1 상담"]')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/toolbar_mypage_text_view'))).click()
					sleep(2)
					# 나의 리뷰 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="나의 리뷰"]')))
					# 고객센터
					scroll_click(self,driver,'com.aritaum1:id/l_lay_customer')
					# 챗봇상담하기 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="챗봇 상담하기"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0073 Passed (Watch Page of Chatbot)")
				pass_check = 1
				break

	def test_74_Consultation(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 1:1 상담
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="1:1 상담"]'))).click()
				sleep(2)
				# 1:1 상담 타이틀
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="1:1 상담"]')))
				# 뒤로 (<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 1:1 상담 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="1:1 상담"]')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/toolbar_mypage_text_view'))).click()
					sleep(2)
					# 나의 리뷰 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="나의 리뷰"]')))
					# 고객센터
					scroll_click(self,driver,'com.aritaum1:id/l_lay_customer')
					# 챗봇상담하기 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="챗봇 상담하기"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0074 Passed (Watch Page of Consultation)")
				pass_check = 1
				break

	def test_75_Notice(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 공지사항 더보기
				scroll_click_xpath(self,driver,'//android.view.View[@text="공지사항 더보기"]')
				# 검색 텍스트 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="검색"]')))
				# 뒤로 (<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 공지사항 더보기 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="공지사항 더보기"]')))
				# 맨위로
				scroll_find_xpath_back(self,driver,'//android.view.View[contains(@text,"온라인 고객센터 대표전화")]')

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/toolbar_mypage_text_view'))).click()
					sleep(2)
					# 나의 리뷰 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="나의 리뷰"]')))
					# 고객센터
					scroll_click(self,driver,'com.aritaum1:id/l_lay_customer')
					# 챗봇상담하기 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="챗봇 상담하기"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0075 Passed (Watch Page of Notice)")
				pass_check = 1
				break


	def test_76_FAQ(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# FAQ
				wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="FAQ"]'))).click()
				sleep(2)
				# 결제/배송 텍스트 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="결제/배송"]')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/toolbar_mypage_text_view'))).click()
					sleep(2)
					# 나의 리뷰 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="나의 리뷰"]')))
					# 고객센터
					scroll_click(self,driver,'com.aritaum1:id/l_lay_customer')
					# 챗봇상담하기 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="챗봇 상담하기"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0076 Passed (Watch List of FAQ)")
				pass_check = 1
				break

	def test_77_FAQ_Other(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# FAQ 더보기
				scroll_click_xpath(self,driver,'//android.view.View[@text="FAQ 더보기"]')
				# 전체 텍스트 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="전체"]')))
				# 뒤로 (<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 공지사항 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="공지사항"]')))
				# 뒤로 (<-)
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_back_image_view'))).click()
				sleep(2)
				# 마이아리따움
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="마이아리따움"]')))

			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					# 마이아리따움
					wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/toolbar_mypage_text_view'))).click()
					sleep(2)
					# 나의 리뷰 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="나의 리뷰"]')))
					# 고객센터
					scroll_click(self,driver,'com.aritaum1:id/l_lay_customer')
					# 챗봇상담하기 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="챗봇 상담하기"]')))
					# FAQ
					wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="FAQ"]'))).click()
					sleep(2)
					# 결제/배송 텍스트 노출
					wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="결제/배송"]')))
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0077 Passed (Watch Page of FAQ Other)")
				pass_check = 1
				break


	def test_78_Logout(self):
		global driver, pass_check
		wait = WebDriverWait(driver, 30)
		loopcount = 0
		pass_check = 0
		while 1:
			try:
				# 장바구니 비우기 #
				# 카트
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_cart_image_view'))).click()
				sleep(2)
				while 1:
					try:
						wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="장바구니에서 상품 삭제"]'))).click()
						sleep(2)
						# 해당 상품을 장바구니에서 삭제하시겠습니까? 창 노출
						wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[contains(@text,"삭제하시겠습니까?")]')))
						# 확인
						wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="확인"]'))).click()
						sleep(2)
					except:
						break
				# 홈으로
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/header_home_image_view'))).click()
				sleep(2)
				# 배너
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/banner_image_view')))
				# 마이아리따움
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/toolbar_mypage_text_view'))).click()
				sleep(2)
				# 나의 리뷰 노출
				wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="나의 리뷰"]')))
				# 로그아웃
				scroll_click(self,driver,'com.aritaum1:id/l_lay_log_out')
				# 로그아웃을 하시겠습니까? 창 노출
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/comment_text_view')))
				# 확인
				wait.until(EC.element_to_be_clickable((By.ID, 'com.aritaum1:id/left_button_text_view'))).click()
				sleep(2)
				# 배너
				wait.until(EC.presence_of_element_located((By.ID, 'com.aritaum1:id/banner_image_view')))
			except:
				if loopcount < 3:
					Exception(self, driver, "home")
					loopcount += 1
					pass
				else:
					self.assertEqual(0, 1)
					break
			else:
				print("ETH_0078 Passed (Check Action of Logout)")
				pass_check = 1
				final_check = 1
				break

	def tearDown(self):
		global ini, driver, final_check, pass_check
		if pass_check == 0:
			driver.launch_app()
			sleep(1)
		if final_check == 1:
			driver.quit()

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(And)
	unittest.TextTestRunner(verbosity=2).run(suite)
# 2020 0303 C6
# 2020 0303 C7
