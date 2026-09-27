from django.core.management.base import BaseCommand
from main.models import (
    Profile,
    BioParagraph,
    Research,
    ResearchTeamMember,
    Project,
    ProjectTeamMember,
    Teaching,
    SocialLink,
    ContactInfo,
)


class Command(BaseCommand):
    help = "Seed database with initial portfolio content matching the existing static site"

    def handle(self, *args, **kwargs):
        # 1. Profile
        Profile.objects.all().delete()
        profile = Profile.objects.create(
            name="Harimohan Khatri",
            role="Educator and Researcher",
            focus_area="Learning Models and Visual Computing",
            profile_image="profile/profile.png",
            email="khatriharimohan@gmail.com",
            work_email="harimohank@nec.edu.np",
            phone="+977 9866108477",
            cv_file="cv/CVHMK.pdf",
            is_active=True,
        )
        self.stdout.write(self.style.SUCCESS(f"Created Profile: {profile.name}"))

        # 2. Bio Paragraphs
        BioParagraph.objects.all().delete()
        paragraphs = [
            "Hello!",
            "My family calls me Hameer; others call me Harimohan. You can call me either or give me a name you like and use that instead.",
            "Biologically, I'm a human male.",
            "Professionally, I'm an educator and researcher. I hold Bachelor's and Master's degree in Computer Engineering from Pokhara University. I teach subjects including data structure and algorithms, artificial intelligence, machine learning, artificial neural networks, database management systems, data science and analytics, big data analytics, data mining, digital image processing, computer vision, computer graphics, cloud computing, and distributed systems.",
            "Currently, I'm exploring the optimization of quantization of neural networks for resource-constrained environments.",
            "Philosophically, I'm just a restless soul within a chunk of soil.",
            "Beyond all these, I'm a cinephile. Movies like Dead Poets Society, Good Will Hunting, Taste of Cherry, and Ship of Theseus have stayed with me, while the works of Christopher Nolan and Abbas Kiarostami continue to inspire me. I read Franz Kafka, and Yuval Noah Harari among others, depending on what kind of questions are occupying my mind at the time.",
            "Also I can cook eatable food.",
            "Talk to me about computer science, astrophysics, quantum mechanics, philosophy, visual and performing arts, literature, or just send memes in my Instagram inbox.",
        ]
        for idx, p_text in enumerate(paragraphs, 1):
            BioParagraph.objects.create(content=p_text, display_order=idx, is_active=True)
        self.stdout.write(self.style.SUCCESS(f"Created {len(paragraphs)} Bio Paragraphs"))

        # 3. Research
        Research.objects.all().delete()
        
        r1 = Research.objects.create(
            title="Transformation Aware Copy-Move Forgery Detection Using Vision Transformer and Keypoint-Based Feature Fusion",
            description="This project explores robust detection of copy-move image forgeries by combining vision transformer representations with keypoint-based feature fusion, aiming to improve resilience against geometric transformations such as rotation, scaling and flipping that typically evade conventional forgery detectors.",
            status="published",
            publication_url="https://github.com",
            display_order=1,
            is_active=True,
        )

        r2 = Research.objects.create(
            title="Sentiment Analysis on Social Media Posts on Romanized-Nepali Texts",
            description="This project analyzes sentiment in social media posts written in Romanized Nepali, addressing the challenges of informal spelling variation, code-mixing and the absence of standardized text normalization tools for low-resource, transliterated language content.",
            status="working",
            display_order=2,
            is_active=True,
        )
        ResearchTeamMember.objects.create(research=r2, name="Harimohan Khatri", role="Team Lead", email="harimohank@nec.edu.np", display_order=1)
        ResearchTeamMember.objects.create(research=r2, name="Team Member 2", role="Role", email="member2@example.com", display_order=2)
        ResearchTeamMember.objects.create(research=r2, name="Team Member 3", role="Role", email="member3@example.com", display_order=3)

        r3 = Research.objects.create(
            title="TinyML Model for Human-Wildlife Conflict Resolution",
            description="This project develops a lightweight, on-device machine learning model to detect and flag early signs of human-wildlife conflict, such as animal proximity to farmland or settlements, enabling timely alerts on low-power edge hardware deployed in affected areas.",
            status="working",
            display_order=3,
            is_active=True,
        )
        ResearchTeamMember.objects.create(research=r3, name="Harimohan Khatri", role="Team Lead", email="harimohank@nec.edu.np", display_order=1)
        ResearchTeamMember.objects.create(research=r3, name="Team Member 2", role="Role", email="member2@example.com", display_order=2)
        ResearchTeamMember.objects.create(research=r3, name="Team Member 3", role="Role", email="member3@example.com", display_order=3)

        r4 = Research.objects.create(
            title="Multimodal RAG System for Domain Specific Knowledge Bases",
            description="This project builds a retrieval-augmented generation system that reasons over multiple modalities, such as text and images, to answer domain-specific queries grounded in a curated knowledge base, reducing hallucination and improving traceability of generated answers.",
            status="working",
            display_order=4,
            is_active=True,
        )
        ResearchTeamMember.objects.create(research=r4, name="Harimohan Khatri", role="Team Lead", email="harimohank@nec.edu.np", display_order=1)
        ResearchTeamMember.objects.create(research=r4, name="Team Member 2", role="Role", email="member2@example.com", display_order=2)
        ResearchTeamMember.objects.create(research=r4, name="Team Member 3", role="Role", email="member3@example.com", display_order=3)

        r5 = Research.objects.create(
            title="Text Message Classifier Model in Low Resource Settings for Receiver End Filtering",
            description="This project designs a compact text message classifier suited for low-resource environments, intended to run on the receiver's end to filter spam, phishing or unwanted messages without relying on cloud processing or heavy computational resources.",
            status="working",
            display_order=5,
            is_active=True,
        )
        ResearchTeamMember.objects.create(research=r5, name="Harimohan Khatri", role="Team Lead", email="harimohank@nec.edu.np", display_order=1)
        ResearchTeamMember.objects.create(research=r5, name="Team Member 2", role="Role", email="member2@example.com", display_order=2)
        ResearchTeamMember.objects.create(research=r5, name="Team Member 3", role="Role", email="member3@example.com", display_order=3)

        self.stdout.write(self.style.SUCCESS("Created 5 Research Items with Team Members"))

        # 4. Projects
        Project.objects.all().delete()

        p1 = Project.objects.create(
            title="Mathema",
            description="Mathematical Equations, Transformation, Algorithms Visualizer tool",
            status="working",
            display_order=1,
            is_active=True,
        )
        ProjectTeamMember.objects.create(project=p1, name="Harimohan Khatri", role="Developer", email="harimohank@nec.edu.np", display_order=1)

        p2 = Project.objects.create(
            title="NLPC",
            description="A Semantic Compilation Framework for Translating Natural Language into Executable Machine Code",
            status="idea",
            collaborate_email="harimohank@nec.edu.np",
            display_order=2,
            is_active=True,
        )

        self.stdout.write(self.style.SUCCESS("Created 2 Projects"))

        # 5. Teaching
        Teaching.objects.all().delete()
        courses = [
            ("Data Science and Analytics", True, "https://github.com", "https://classroom.google.com"),
            ("Computer Graphics", True, "https://github.com", "https://classroom.google.com"),
            ("Data Structure and Algorithms", False, "https://github.com", None),
            ("Artificial Intelligence", False, "https://github.com", None),
            ("Machine Learning", False, "https://github.com", None),
            ("Artificial Neural Networks", False, "https://github.com", None),
            ("Database Management Systems", False, "https://github.com", None),
            ("Big Data Analytics", False, "https://github.com", None),
            ("Data Mining", False, "https://github.com", None),
            ("Digital Image Processing", False, "https://github.com", None),
            ("Computer Vision", False, "https://github.com", None),
            ("Cloud Computing", False, "https://github.com", None),
            ("Distributed Systems", False, "https://github.com", None),
        ]
        for idx, (name, active_sem, mats, classroom) in enumerate(courses, 1):
            Teaching.objects.create(
                course_name=name,
                is_active_semester=active_sem,
                materials_url=mats,
                classroom_url=classroom,
                display_order=idx,
                is_active=True,
            )
        self.stdout.write(self.style.SUCCESS(f"Created {len(courses)} Teaching Courses"))

        # 6. Social Links
        SocialLink.objects.all().delete()
        socials = [
            ("LinkedIn", "https://www.linkedin.com", "social_icons/linkedin.svg", "linkedin.svg"),
            ("Google Scholar", "https://scholar.google.com", "social_icons/google-scholar.svg", "google-scholar.svg"),
            ("GitHub", "https://github.com", "social_icons/github.svg", "github.svg"),
            ("ORCID", "https://orcid.org", "social_icons/orcid.svg", "orcid.svg"),
        ]
        for idx, (platform, url, icon_file, static_name) in enumerate(socials, 1):
            SocialLink.objects.create(
                platform=platform,
                url=url,
                icon=icon_file,
                icon_static_name=static_name,
                display_order=idx,
                is_active=True,
            )
        self.stdout.write(self.style.SUCCESS("Created 4 Social Links"))

        # 7. Contact Info
        ContactInfo.objects.all().delete()
        contacts = [
            ("email", "Personal Email", "khatriharimohan@gmail.com", "mailto:khatriharimohan@gmail.com", "mail"),
            ("email", "Work Email", "harimohank@nec.edu.np", "mailto:harimohank@nec.edu.np", "mail"),
            ("phone", "Mobile", "+977 9866108477", "tel:+9779866108477", "phone"),
        ]
        for idx, (ctype, label, val, link, icon) in enumerate(contacts, 1):
            ContactInfo.objects.create(
                contact_type=ctype,
                label=label,
                value=val,
                link_url=link,
                lucide_icon=icon,
                display_order=idx,
                is_active=True,
            )
        self.stdout.write(self.style.SUCCESS("Created 3 Contact Info items"))
        self.stdout.write(self.style.SUCCESS("Initial portfolio database seeding complete!"))
