Tensorflow implementation of [Deep Convolutional Generative Adversarial Networks](http://arxiv.org/abs/1511.06434)

This is the original DCGAN project with some little modification. I just remove the Mnist part of code and change the learning rate.

The original DCGAN code is here https://github.com/carpedm20/DCGAN-tensorflow

What my experiment is refer to https://zhuanlan.zhihu.com/p/24767059?group_id=833793028778000384
, but I am failed in running my own image. The problem of original code is that the loss can not converges and with terrible performance. So I did this modification and results showed well. But I still don't know the reason, if you did please contact to me.

We can use this code to run your own image and generate the same looks image. Just save your image in ./dataset/faces/ and run the main.py with  run.txt

python main.py \
	--image_size 96 \
	--output_size 64 \
	--dataset faces \
	--input_fname_pattern "*.jpg" \
	--sample_dir samples_faces \
	--is_crop True \
	--is_train True \
	--epoch 25

More information just refer to https://github.com/carpedm20/DCGAN-tensorflow
