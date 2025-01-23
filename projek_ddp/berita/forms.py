from django import forms

class CalorieForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Laki-laki'),
        ('female', 'Perempuan'),
    ]

    ACTIVITY_CHOICES = [
        (1.2, 'Sedentary (Jarang Beraktivitas)'),
        (1.375, 'Ringan (Olahraga ringan 1-3 hari/minggu)'),
        (1.55, 'Sedang (Olahraga sedang 3-5 hari/minggu)'),
        (1.725, 'Aktif (Olahraga berat 6-7 hari/minggu)'),
        (1.9, 'Sangat Aktif (Olahraga sangat berat/pekerjaan fisik)'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Jenis Kelamin", required=True)
    age = forms.IntegerField(label="Umur (tahun)", min_value=1, required=True)
    weight = forms.FloatField(label="Berat Badan (kg)", min_value=1.0, required=True)
    height = forms.FloatField(label="Tinggi Badan (cm)", min_value=1.0, required=True)
    activity_level = forms.ChoiceField(choices=ACTIVITY_CHOICES, label="Tingkat Aktivitas", required=True)

class MuscleForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Laki-laki'),
        ('female', 'Perempuan'),
    ]
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, 
        label="Jenis Kelamin", 
        widget=forms.Select(attrs={"class": "form-select"})
    )
    weight = forms.FloatField(
        label="Berat Badan (kg)", 
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Masukkan berat badan Anda"})
    )
    height = forms.FloatField(
        label="Tinggi Badan (cm)", 
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Masukkan tinggi badan Anda"})
    )