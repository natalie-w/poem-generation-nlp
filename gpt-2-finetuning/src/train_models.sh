#train models

for batch in 1 16 32 64 128


do
	for learn_rate in 1 0.5 0.25 0.1 0.05
	
	do 

		echo "Training model with batch $batch and learning rate $learn_rate"
		python train.py --dataset poems.npz --batch_size $batch --learning_rate $learn_rate --save_every 100 --run_name "run batch$batch lr$learn_rate"
	
	done

	echo "woohoo"

done

Echo "done"