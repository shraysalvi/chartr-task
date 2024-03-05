from rest_framework.test import APITestCase
from rest_framework import status
from .models import Note
from django.urls import reverse


class NoteViewSetTests(APITestCase):
    def setUp(self):
        self.note1 = Note.objects.create(title='Test Note 1', body='Body of Test Note 1')
        self.note2 = Note.objects.create(title='Test Note 2', body='Body of Test Note 2')

    def test_filter_notes_by_title(self):
        response = self.client.get(reverse('note-list'), {'title': 'Test Note 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Note 1')
        
    def test_get_notes(self):
        response = self.client.get(reverse('note-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_note_detail(self):
        url = reverse('note-detail', kwargs={'pk': self.note1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Note 1')

    def test_create_note(self):
        data = {'title': 'New Note', 'body': 'Body of New Note'}
        response = self.client.post(reverse('note-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 3) 

    def test_update_note(self):
        url = reverse('note-detail', kwargs={'pk': self.note1.pk})
        data = {'title': 'Updated Title', 'body': 'Updated Body'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_partial_update_note(self):
        url = reverse('note-detail', kwargs={'pk': self.note1.pk})
        data = {'title': 'Partial Update'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Partial Update')

    def test_delete_note(self):
        url = reverse('note-detail', kwargs={'pk': self.note1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 1)
