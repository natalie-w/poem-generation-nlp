#train models

#for batch in 2 3 4 5


#do
	for learn_rate in 0.001 0.0005 0.0001 0.00005 0.00001
	
	do 

		echo "Training model with batch 1  and learning rate $learn_rate"
		python train.py --dataset poems.npz --learning_rate $learn_rate --save_every 100 --run_name "run batch$batch lr$learn_rate"
	
	done

	echo "woohoo"

done

Echo "done"
