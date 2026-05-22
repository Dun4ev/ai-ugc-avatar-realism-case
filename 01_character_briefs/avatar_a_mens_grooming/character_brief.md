# Avatar A: Men's Grooming Advisor

## Суть персонажа

Avatar A — спокойный и уверенный men's grooming advisor для UGC-style контента о face wash, beard care, moisturizer, shaving и fragrance/body care.

## Роль в кейсе

Этот аватар используется как первый тестовый персонаж для проверки pipeline:

- base portrait reference;
- диагностика реализма кожи, глаз, губ и бороды;
- comparison grid;
- будущий image-to-video test.

## Визуальная цель

Персонаж должен выглядеть не как generic AI influencer, а как реалистичный человек в premium but approachable grooming-сценарии.

Ключевые признаки:

- натуральная текстура кожи;
- глаза без стеклянного эффекта;
- губы без rubber/smoothed эффекта;
- борода без painted/flickering эффекта;
- спокойная мужская grooming-эстетика;
- пригодность для короткого UGC-style video test.

## Риски реализма

| Риск | Что смотреть |
|---|---|
| plastic_skin | Слишком гладкая кожа, отсутствие пор и тональных вариаций. |
| glassy_eyes | Искусственный блеск, неживой взгляд. |
| rubber_lips | Слишком сглаженные губы и неестественный контур. |
| beard_artifacts | Нарисованная или неоднородная борода. |
| identity_drift | Изменение лица между base, realism pass и final still. |

## Текущий статус

На 2026-05-20 добавлен первый men's grooming portrait reference из Pexels.

Файл используется как начальная рабочая точка:

- source reference: `02_source_data/public_references/pexels_unsplash/mens_grooming_pexels_001.jpg`
- base avatar: `03_base_avatars/avatar_a_mens_grooming/selected/base.jpg`
- current final placeholder: `04_realism_passes/avatar_a_mens_grooming/final_stills/final.jpg`

Важно: текущий `final.jpg` является тем же изображением, что и `base.jpg`. Его нельзя считать результатом реального realism pass.
