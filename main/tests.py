from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education, AboutTrait


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def _get_experience_json(self):
        """Ambil data experience dari endpoint JSON, dikunci berdasarkan pk."""
        response = self.client.get("/api/experience/")
        self.assertEqual(response.status_code, 200)
        return {item["pk"]: item["fields"] for item in response.json()}

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        # 1) Halaman HTML: hanya rangka statis (kartu diisi JS)
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        # 2) Data: dari endpoint JSON
        exp = self._get_experience_json()[str(self.experience.id)]
        self.assertEqual(exp["title"], self.experience.title)
        self.assertEqual(exp["description"], self.experience.description)
        self.assertEqual(exp["category"], "part-time")
        self.assertEqual(exp["ended_at"], "")    # kosong -> "Sedang berlangsung" di JS
        self.assertTrue(exp["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get("/api/experience/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        self.assertFalse(self.experience.is_ongoing)

        exp = self._get_experience_json()[str(self.experience.id)]
        self.assertNotEqual(exp["ended_at"], "")  # terisi -> "Selesai: ..." di JS
        self.assertFalse(exp["is_ongoing"])


class EducationTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            level_type="Higher Education",
            title="Bachelor of Information Systems",
            institution="Universitas Indonesia",
            start_year=2025,
            end_year="Present",
            description="Exploring the intersection of technology, data, and people.",
            tags="Information Systems, Technology, Data",
            color_theme="amber",
        )

    def test_education_model(self):
        self.assertEqual(str(self.education), "Bachelor of Information Systems - Universitas Indonesia")
        self.assertEqual(self.education.color_theme, "amber")
        self.assertEqual(self.education.get_tags_list(), ["Information Systems", "Technology", "Data"])

    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, self.education.title)
        self.assertContains(response, self.education.institution)
        self.assertContains(response, self.education.description)
        self.assertContains(response, "Information Systems")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "Belum ada data pendidikan yang ditambahkan.")


class AboutTest(TestCase):
    def setUp(self):
        self.trait = AboutTrait.objects.create(
            emoji="⚙️",
            title="Systems Thinker",
            description="Curious about how systems, databases, and technology work together.",
        )

    def test_about_model(self):
        self.assertEqual(str(self.trait), "Systems Thinker")
        self.assertEqual(self.trait.emoji, "⚙️")

    def test_about_page(self):
        response = self.client.get(reverse("main:show_about"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")
        self.assertContains(response, self.trait.title)
        self.assertContains(response, self.trait.description)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_about_page(self):
        AboutTrait.objects.all().delete()
        response = self.client.get(reverse("main:show_about"))

        self.assertContains(response, "Belum ada informasi sifat yang ditambahkan.")