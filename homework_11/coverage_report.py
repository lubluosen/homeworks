import coverage
import unittest

# Создаем объект покрытия
cov = coverage.Coverage()
cov.start()

# Запускаем все тесты в проекте
loader = unittest.TestLoader()
tests = loader.discover(start_dir='.', pattern='test_*.py')
testRunner = unittest.TextTestRunner()
testRunner.run(tests)

cov.stop()
cov.save()

# Печатаем отчет о покрытии
cov.report()

# Генерируем HTML отчет
cov.html_report(directory='coverage_report')