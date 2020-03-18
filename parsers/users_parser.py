from flask_restful import reqparse


post_parser = reqparse.RequestParser()
post_parser.add_argument('surname', required=True)
post_parser.add_argument('name', required=True)
post_parser.add_argument('age', required=True, type=int)
post_parser.add_argument('position', required=True)
post_parser.add_argument('speciality', required=True)
post_parser.add_argument('address', required=True)
post_parser.add_argument('email', required=True)
post_parser.add_argument('password', required=True)
post_parser.add_argument('user_id', type=int)
post_parser.add_argument('city_from')

put_parser = reqparse.RequestParser()
put_parser.add_argument('surname')
put_parser.add_argument('name')
put_parser.add_argument('age', type=int)
put_parser.add_argument('position')
put_parser.add_argument('speciality')
put_parser.add_argument('address')
put_parser.add_argument('email')
put_parser.add_argument('password')
put_parser.add_argument('city_from')