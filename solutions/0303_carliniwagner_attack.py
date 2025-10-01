### L2CarliniWagner attack
epsilons = [0.1, 0.3, 0.5, 0.9]

cwattack = foolbox.attacks.L2CarliniWagnerAttack(steps=1000)
raw_advs_images, advs_images, success = cwattack(model=fmodel, inputs=example_image, criterion=criterion, epsilons=epsilons)
