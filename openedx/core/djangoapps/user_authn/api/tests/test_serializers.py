"""Tests for serializers for the MFE Context"""
import json

from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse
from rest_framework import status

from openedx.core.djangoapps.user_authn.serializers import MFEContextSerializer


class TestMFEContextSerializer(TestCase):
    """
    High-level unit tests for MFEContextSerializer
    """

    def setUp(self):
        """
        Set up tests
        """
        super().setUp()
        self.url = reverse('mfe_context')
        self.query_params = {'next': '/dashboard'}

        print("\n\n\nURL", self.url, "\n\n\n")

    @staticmethod
    def get_mock_mfe_context_data():
        """
        Helper function to generate mock data for the MFE Context API view.
        """

        mock_context_data = {
            'context_data': {
                'currentProvider': 'edX',
                'platformName': 'edX',
                'providers': [
                    {
                        'id': 'oa2-facebook',
                        'name': 'Facebook',
                        'iconClass': 'fa-facebook',
                        'iconImage': None,
                        'skipHintedLogin': False,
                        'skipRegistrationForm': False,
                        'loginUrl': 'https://facebook.com/login',
                        'registerUrl': 'https://facebook.com/register'
                    },
                    {
                        'id': 'oa2-google-oauth2',
                        'name': 'Google',
                        'iconClass': 'fa-google-plus',
                        'iconImage': None,
                        'skipHintedLogin': False,
                        'skipRegistrationForm': False,
                        'loginUrl': 'https://google.com/login',
                        'registerUrl': 'https://google.com/register'
                    }
                ],
                'secondaryProviders': [],
                'finishAuthUrl': 'https://edx.com/auth/finish',
                'errorMessage': None,
                'registerFormSubmitButtonText': 'Create Account',
                'autoSubmitRegForm': False,
                'syncLearnerProfileData': False,
                'countryCode': '',
                'pipeline_user_details': {
                    'username': 'test123',
                    'email': 'test123@edx.com',
                    'fullname': 'Test Test',
                    'first_name': 'Test',
                    'last_name': 'Test'
                }
            },
            'registration_fields': {},
            'optional_fields': {
                'extended_profile': []
            }
        }

        return mock_context_data

    @staticmethod
    def get_mock_empty_mfe_context_data():
        """
        Helper function to generate mock empty data for the MFE Context API view.
        """

        mock_context_data = {
            'context_data': {
                'currentProvider': None,
                'platformName': 'édX',
                'providers': [],
                'secondaryProviders': [],
                'finishAuthUrl': None,
                'errorMessage': None,
                'registerFormSubmitButtonText': 'Create Account',
                'autoSubmitRegForm': False,
                'syncLearnerProfileData': False,
                'countryCode': '',
                'pipeline_user_details': {}
            },
            'registration_fields': {},
            'optional_fields': {
                'extended_profile': []
            }
        }

        return mock_context_data

    @staticmethod
    def get_expected_data():
        """
        Helper function to generate expected data for the MFE Context API view serializer.
        """

        expected_data = {
            'contextData': {
                'currentProvider': 'edX',
                'platformName': 'edX',
                'providers': [
                    {
                        'id': 'oa2-facebook',
                        'name': 'Facebook',
                        'iconClass': 'fa-facebook',
                        'iconImage': None,
                        'skipHintedLogin': False,
                        'skipRegistrationForm': False,
                        'loginUrl': 'https://facebook.com/login',
                        'registerUrl': 'https://facebook.com/register'
                    },
                    {
                        'id': 'oa2-google-oauth2',
                        'name': 'Google',
                        'iconClass': 'fa-google-plus',
                        'iconImage': None,
                        'skipHintedLogin': False,
                        'skipRegistrationForm': False,
                        'loginUrl': 'https://google.com/login',
                        'registerUrl': 'https://google.com/register'
                    }
                ],
                'secondaryProviders': [],
                'finishAuthUrl': 'https://edx.com/auth/finish',
                'errorMessage': None,
                'registerFormSubmitButtonText': 'Create Account',
                'autoSubmitRegForm': False,
                'syncLearnerProfileData': False,
                'countryCode': '',
                'pipelineUserDetails': {
                    'username': 'test123',
                    'email': 'test123@edx.com',
                    'name': 'Test Test',
                    'firstName': 'Test',
                    'lastName': 'Test'
                }
            },
            'registrationFields': {},
            'optionalFields': {
                'extended_profile': []
            }
        }

        return expected_data

    @staticmethod
    def get_empty_expected_data():
        """
        Helper function to generate empty expected data for the MFE Context API view serializer.
        """

        expected_data = {
            'contextData': {
                'currentProvider': None,
                'platformName': 'édX',
                'providers': [],
                'secondaryProviders': [],
                'finishAuthUrl': None,
                'errorMessage': None,
                'registerFormSubmitButtonText': 'Create Account',
                'autoSubmitRegForm': False,
                'syncLearnerProfileData': False,
                'countryCode': '',
                'pipelineUserDetails': {}
            },
            'registrationFields': {},
            'optionalFields': {
                'extended_profile': []
            }
        }

        return expected_data

    def test_mfe_context_serializer(self):
        """
        Test MFEContextSerializer with mock data that serializes data correctly
        """

        print("\n\n\nURL", self.url, "\n\n\n")
        mfe_context_data = self.get_mock_mfe_context_data()
        expected_data = self.get_expected_data()
        output_data = MFEContextSerializer(
            mfe_context_data
        ).data

        self.assertDictEqual(
            output_data,
            expected_data
        )

    def test_get_mfe_context_response_keys(self):
        print("\n\n\nURL", self.url, "\n\n\n")
        response = self.client.get(self.url, self.query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_keys = ['contextData', 'registrationFields', 'optionalFields']
        for key in expected_keys:
            self.assertIn(key, response.data)

    @override_settings(
        ENABLE_DYNAMIC_REGISTRATION_FIELDS=True,
        REGISTRATION_EXTRA_FIELDS={'state': 'required', 'last_name': 'required', 'first_name': 'required'},
        REGISTRATION_FIELD_ORDER=['first_name', 'last_name', 'state'],
    )
    def test_mfe_context_serializer_empty_response(self):
        print("\n\n\nURL", self.url, "\n\n\n")
        mfe_context_data = self.get_mock_empty_mfe_context_data()
        expected_data = self.get_empty_expected_data()
        serialized_data = MFEContextSerializer(
            mfe_context_data
        ).data

        self.assertDictEqual(
            serialized_data,
            expected_data
        )

    @override_settings(
        ENABLE_DYNAMIC_REGISTRATION_FIELDS=True,
        REGISTRATION_EXTRA_FIELDS={'state': 'required', 'last_name': 'required', 'first_name': 'required'},
        REGISTRATION_FIELD_ORDER=['first_name', 'last_name', 'state'],
    )
    def test_mfe_context_api_response(self):
        print("\n\n\nURL", self.url, "\n\n\n")
        response = self.client.get(self.url, self.query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serialized_data = json.loads(response.content)
        expected_data = self.get_empty_expected_data()

        self.assertEqual(
            serialized_data,
            expected_data
        )
